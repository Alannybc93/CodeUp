# usuarios/views.py - VERSÃO COMPLETA
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models import Q
from datetime import timedelta
import json

from .models import Perfil, LinkSocial, AtividadePerfil

# REMOVA A LINHA "import forms" e use:
from django import forms

User = get_user_model()

# ==================== HELPER FUNCTIONS ====================
def get_user_perfil(user):
    """Obtém ou cria o perfil do usuário"""
    perfil, created = Perfil.objects.get_or_create(usuario=user)
    return perfil

# ==================== DECORATORS ====================
def nivel_requerido(nivel_minimo):
    """Decorator para verificar nível do usuário"""
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            usuario = request.user
            if not usuario.is_authenticated:
                return redirect('usuarios:login')
            
            perfil = get_user_perfil(usuario)
            nivel_atual = perfil.nivel
            
            if nivel_atual >= nivel_minimo:
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, 'Você não tem permissão para acessar esta página.')
                return redirect('usuarios:acesso_negado')
        return _wrapped_view
    return decorator

# ==================== PÁGINAS BÁSICAS ====================
def home(request):
    """Página inicial do CodeUp"""
    return render(request, 'inicio.html')

def acesso_negado(request):
    """Página de acesso negado"""
    return render(request, 'usuarios/acesso_negado.html')

# ==================== AUTENTICAÇÃO ====================
def login_view(request):
    """View de login"""
    if request.user.is_authenticated:
        perfil = get_user_perfil(request.user)
        if not perfil.jornada_iniciada:
            return redirect('usuarios:iniciar_jornada')
        return redirect('usuarios:dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo de volta, {user.username}!')
            
            user.last_login = timezone.now()
            user.save(update_fields=['last_login'])
            
            perfil = get_user_perfil(user)
            AtividadePerfil.objects.create(
                perfil=perfil,
                tipo='login',
                titulo='Login realizado',
                descricao='Você fez login no sistema.'
            )
            
            if not perfil.jornada_iniciada:
                return redirect('usuarios:iniciar_jornada')
            
            return redirect('usuarios:dashboard')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    
    return render(request, 'usuarios/login.html')

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

def registrar(request):
    """View de registro"""
    if request.user.is_authenticated:
        messages.info(request, "Você já está logado!")
        return redirect('inicio')
    
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            perfil = get_user_perfil(user)
            login(request, user)
            
            AtividadePerfil.objects.create(
                perfil=perfil,
                tipo='sistema',
                titulo='Conta criada',
                descricao='Bem-vindo ao CodeUp!'
            )
            
            messages.success(request, f"Conta criada com sucesso! Bem-vindo(a) ao CodeUp, {user.username}!")
            return redirect('usuarios:iniciar_jornada')
    else:
        form = RegistroForm()
    
    return render(request, 'usuarios/registrar.html', {'form': form})

# ==================== LOGOUT ====================
@require_http_methods(["GET", "POST"])
@login_required
def logout_view(request):
    """View de logout"""
    perfil = get_user_perfil(request.user)
    AtividadePerfil.objects.create(
        perfil=perfil,
        tipo='login',
        titulo='Logout realizado',
        descricao='Você saiu do sistema.'
    )
    
    logout(request)
    messages.success(request, 'Você saiu da sua conta com sucesso!')
    return redirect('inicio')

# ==================== JORNADA INICIAL ====================
@login_required
def iniciar_jornada(request):
    """Inicia a jornada do usuário"""
    usuario = request.user
    perfil = get_user_perfil(usuario)
    
    if perfil.jornada_iniciada:
        return redirect('usuarios:dashboard')
    
    perfil.jornada_iniciada = True
    perfil.xp = 100
    perfil.save(update_fields=['jornada_iniciada', 'xp'])
    
    AtividadePerfil.objects.create(
        perfil=perfil,
        tipo='sistema',
        titulo='Jornada Iniciada',
        descricao='Você iniciou sua jornada no CodeUp! Ganhou 100 XP.'
    )
    
    messages.success(request, '🎉 Jornada iniciada! Você ganhou 100 XP!')
    return redirect('usuarios:tutorial_inicial')

@login_required
def tutorial_inicial(request):
    """Tutorial inicial"""
    usuario = request.user
    perfil = get_user_perfil(usuario)
    
    if not perfil.jornada_iniciada:
        return redirect('usuarios:iniciar_jornada')
    
    etapas = [
        {
            'numero': 1,
            'icone': 'fa-user',
            'titulo': 'Complete seu perfil',
            'descricao': 'Adicione uma foto e informações sobre você',
            'acao': 'editar_perfil',
            'concluida': bool(usuario.first_name or perfil.bio)
        },
        {
            'numero': 2,
            'icone': 'fa-graduation-cap',
            'titulo': 'Explore as trilhas',
            'descricao': 'Conheça os caminhos de aprendizado disponíveis',
            'acao': 'explorar_trilhas',
            'concluida': False
        },
        {
            'numero': 3,
            'icone': 'fa-code',
            'titulo': 'Resolva um exercício',
            'descricao': 'Pratique com exercícios interativos',
            'acao': 'explorar_exercicios',
            'concluida': False
        }
    ]
    
    context = {
        'usuario': usuario,
        'perfil': perfil,
        'etapas': etapas,
        'etapas_concluidas': sum(1 for e in etapas if e['concluida']),
        'total_etapas': len(etapas),
    }
    
    return render(request, 'usuarios/tutorial_inicial.html', context)

@login_required
def concluir_tutorial(request):
    """Marca tutorial como concluído"""
    if request.method == 'POST':
        usuario = request.user
        perfil = get_user_perfil(usuario)
        
        perfil.xp += 200
        perfil.save(update_fields=['xp'])
        
        request.session['tutorial_concluido'] = True
        
        AtividadePerfil.objects.create(
            perfil=perfil,
            tipo='conquista',
            titulo='Tutorial Concluído',
            descricao='Você completou o tutorial inicial! Ganhou 200 XP.'
        )
        
        messages.success(request, '🎓 Tutorial concluído! +200 XP!')
        return redirect('usuarios:dashboard')
    
    return redirect('usuarios:tutorial_inicial')

# ==================== DASHBOARD ====================
@login_required
def dashboard(request):
    """Dashboard principal"""
    usuario = request.user
    perfil = get_user_perfil(usuario)
    
    if not perfil.jornada_iniciada:
        return redirect('usuarios:iniciar_jornada')
    
    nivel = perfil.nivel
    xp = perfil.xp
    trilhas_concluidas = perfil.trilhas_concluidas
    exercicios_resolvidos = perfil.exercicios_resolvidos
    
    xp_necessario = nivel * 1000
    progresso_nivel = min(int((xp / xp_necessario) * 100), 100) if xp_necessario > 0 else 0
    
    atividades_recentes = perfil.atividades.all()[:10]
    
    context = {
        'usuario': usuario,
        'perfil': perfil,
        'nivel': nivel,
        'xp': xp,
        'trilhas_concluidas': trilhas_concluidas,
        'exercicios_resolvidos': exercicios_resolvidos,
        'progresso_nivel': progresso_nivel,
        'xp_necessario': xp_necessario,
        'xp_faltante': max(0, xp_necessario - xp),
        'atividades_recentes': atividades_recentes,
        'is_admin': perfil.nivel >= 50 or usuario.is_superuser,
    }
    
    return render(request, 'usuarios/dashboard.html', context)

# ==================== PERFIL ====================
@login_required
def perfil(request):
    """Página do perfil"""
    usuario = request.user
    perfil = get_user_perfil(usuario)
    
    if not perfil.jornada_iniciada:
        return redirect('usuarios:iniciar_jornada')
    
    dados_perfil = {
        'nome_completo': perfil.nome_completo(),
        'email': usuario.email,
        'data_cadastro': usuario.date_joined.strftime('%d/%m/%Y'),
        'nivel': perfil.nivel,
        'xp': perfil.xp,
        'trilhas_concluidas': perfil.trilhas_concluidas,
        'exercicios_resolvidos': perfil.exercicios_resolvidos,
        'bio': perfil.bio,
        'jornada_iniciada': perfil.jornada_iniciada,
    }
    
    xp_necessario = perfil.nivel * 1000
    dados_perfil['progresso_nivel'] = min(int((perfil.xp / xp_necessario) * 100), 100) if xp_necessario > 0 else 0
    
    links_sociais = perfil.links_sociais.filter(ativo=True).order_by('ordem')
    atividades = perfil.atividades.all()[:10]
    
    context = {
        'usuario': usuario,
        'perfil': perfil,
        'dados': dados_perfil,
        'links_sociais': links_sociais,
        'atividades': atividades,
    }
    
    return render(request, 'usuarios/perfil.html', context)

@login_required
def editar_perfil(request):
    """Editar informações do perfil"""
    usuario = request.user
    perfil = get_user_perfil(usuario)
    
    if request.method == 'POST':
        usuario.first_name = request.POST.get('first_name', '').strip()
        usuario.last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        
        try:
            validate_email(email)
            usuario.email = email
        except ValidationError:
            messages.error(request, 'Por favor, insira um e-mail válido.')
            return redirect('usuarios:editar_perfil')
        
        perfil.bio = request.POST.get('bio', '').strip()
        perfil.data_nascimento = request.POST.get('data_nascimento') or None
        
        usuario.save()
        perfil.save()
        
        AtividadePerfil.objects.create(
            perfil=perfil,
            tipo='perfil',
            titulo='Perfil atualizado',
            descricao='Informações pessoais alteradas.'
        )
        
        messages.success(request, 'Perfil atualizado com sucesso!')
        return redirect('usuarios:perfil')
    
    context = {
        'usuario': usuario,
        'perfil': perfil,
    }
    
    return render(request, 'usuarios/editar_perfil.html', context)

@login_required
def alterar_senha(request):
    """Alterar senha do usuário"""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            
            perfil = get_user_perfil(user)
            AtividadePerfil.objects.create(
                perfil=perfil,
                tipo='perfil',
                titulo='Senha alterada',
                descricao='Senha de acesso modificada.'
            )
            
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return redirect('usuarios:perfil')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'usuarios/alterar_senha.html', {'form': form})

@login_required
def excluir_conta(request):
    """Excluir conta do usuário"""
    if request.method == 'POST':
        confirmacao = request.POST.get('confirmacao', '').strip().upper()
        senha_atual = request.POST.get('senha_atual', '')
        
        if confirmacao == "EXCLUIR" and request.user.check_password(senha_atual):
            usuario = request.user
            username = usuario.username
            usuario.delete()
            logout(request)
            messages.success(request, f'Sua conta foi excluída com sucesso. Até breve, {username}!')
            return redirect('inicio')
        else:
            messages.error(request, 'Confirmação incorreta ou senha inválida.')
            return redirect('usuarios:configurar_conta')
    
    return render(request, 'usuarios/excluir_conta.html')

@login_required
def configurar_conta(request):
    """Configurações da conta"""
    usuario = request.user
    
    if request.method == 'POST':
        if 'update_info' in request.POST:
            novo_username = request.POST.get('username', '').strip()
            novo_email = request.POST.get('email', '').strip()
            senha_atual = request.POST.get('current_password', '')
            
            errors = []
            
            if not senha_atual:
                errors.append("Digite sua senha atual para confirmar.")
            elif not usuario.check_password(senha_atual):
                errors.append("Senha atual incorreta.")
            
            if novo_username != usuario.username:
                if User.objects.filter(username=novo_username).exists():
                    errors.append("Este nome de usuário já está em uso.")
            
            if novo_email != usuario.email:
                try:
                    validate_email(novo_email)
                    if User.objects.filter(email=novo_email).exists():
                        errors.append("Este e-mail já está em uso.")
                except ValidationError:
                    errors.append("E-mail inválido.")
            
            if not errors:
                usuario.username = novo_username
                usuario.email = novo_email
                usuario.save()
                messages.success(request, 'Informações atualizadas com sucesso!')
            else:
                for error in errors:
                    messages.error(request, error)
        
        elif 'change_password' in request.POST:
            form = PasswordChangeForm(usuario, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, usuario)
                messages.success(request, 'Senha alterada com sucesso!')
            else:
                for error in form.errors.values():
                    messages.error(request, error)
    
    context = {
        'usuario': usuario,
    }
    
    return render(request, 'usuarios/configurar_conta.html', context)

# ==================== PERFIL PÚBLICO ====================
@login_required
def perfil_publico(request, username=None):
    """Perfil público do usuário"""
    if username:
        usuario_alvo = get_object_or_404(User, username=username)
    else:
        usuario_alvo = request.user
    
    perfil = get_user_perfil(usuario_alvo)
    
    dados_publicos = {
        'nome': usuario_alvo.username,
        'nome_completo': perfil.nome_completo(),
        'nivel': perfil.nivel,
        'trilhas_concluidas': perfil.trilhas_concluidas,
        'exercicios_resolvidos': perfil.exercicios_resolvidos,
        'bio': perfil.bio if perfil.bio else 'Este usuário ainda não escreveu uma biografia.',
        'data_cadastro': usuario_alvo.date_joined.strftime('%d/%m/%Y'),
        'pode_editar': usuario_alvo == request.user,
    }
    
    return render(request, 'usuarios/perfil_publico.html', {
        'usuario_publico': usuario_alvo,
        'dados': dados_publicos
    })

# ==================== FUNÇÕES DE APOIO ====================
@login_required
def adicionar_xp(request, usuario_id=None):
    """Adiciona XP ao perfil do usuário"""
    if usuario_id:
        # Admin adicionando XP para outro usuário
        usuario_alvo = get_object_or_404(User, id=usuario_id)
        perfil = get_user_perfil(usuario_alvo)
        
        # Verificar se é admin
        perfil_admin = get_user_perfil(request.user)
        if perfil_admin.nivel < 50:
            messages.error(request, 'Apenas administradores podem adicionar XP a outros usuários.')
            return redirect('usuarios:perfil')
    else:
        # Usuário adicionando XP para si mesmo
        perfil = get_user_perfil(request.user)
    
    quantidade = 100  # XP padrão
    
    if request.method == 'POST':
        quantidade = int(request.POST.get('quantidade', 100))
    
    perfil.xp += quantidade
    perfil.save()
    
    AtividadePerfil.objects.create(
        perfil=perfil,
        tipo='conquista',
        titulo='XP Adicionado',
        descricao=f'Você ganhou {quantidade} XP!'
    )
    
    messages.success(request, f'+{quantidade} XP adicionados!')
    
    if usuario_id:
        return redirect('usuarios:detalhes_usuario', usuario_id=usuario_id)
    return redirect('usuarios:perfil')

# ==================== VIEWS ADMINISTRATIVAS (SIMPLIFICADAS) ====================
@login_required
@nivel_requerido(50)
def painel_admin(request):
    """Painel administrativo"""
    perfil = get_user_perfil(request.user)
    
    total_usuarios = User.objects.count()
    usuarios_ativos = User.objects.filter(is_active=True).count()
    novos_hoje = User.objects.filter(date_joined__date=timezone.now().date()).count()
    
    context = {
        'usuario': request.user,
        'perfil': perfil,
        'total_usuarios': total_usuarios,
        'usuarios_ativos': usuarios_ativos,
        'novos_hoje': novos_hoje,
    }
    
    return render(request, 'usuarios/admin/painel.html', context)

@login_required
@nivel_requerido(50)
def gerenciar_usuarios(request):
    """Gerenciar usuários"""
    usuarios = User.objects.all().order_by('-date_joined')
    
    usuarios_com_perfil = []
    for user in usuarios:
        try:
            perfil = user.perfil
            usuarios_com_perfil.append({
                'user': user,
                'perfil': perfil
            })
        except:
            usuarios_com_perfil.append({
                'user': user,
                'perfil': None
            })
    
    context = {
        'usuarios': usuarios_com_perfil,
        'total_usuarios': len(usuarios_com_perfil),
    }
    
    return render(request, 'usuarios/admin/gerenciar_usuarios.html', context)

@login_required
@nivel_requerido(50)
def detalhes_usuario(request, usuario_id):
    """Detalhes de um usuário"""
    usuario_alvo = get_object_or_404(User, id=usuario_id)
    perfil_alvo = get_user_perfil(usuario_alvo)
    perfil_admin = get_user_perfil(request.user)
    
    context = {
        'usuario_alvo': usuario_alvo,
        'perfil_alvo': perfil_alvo,
        'perfil_admin': perfil_admin,
        'is_super_admin': perfil_admin.nivel >= 99 or request.user.is_superuser,
    }
    
    return render(request, 'usuarios/admin/detalhes_usuario.html', context)

# Views administrativas simplificadas (para depois implementar)
@login_required
@nivel_requerido(99)
def editar_usuario_admin(request, usuario_id):
    """Editar usuário como admin"""
    messages.info(request, 'Funcionalidade em desenvolvimento.')
    return redirect('usuarios:detalhes_usuario', usuario_id=usuario_id)

@login_required
@nivel_requerido(99)
def resetar_senha_admin(request, usuario_id):
    """Resetar senha como admin"""
    messages.info(request, 'Funcionalidade em desenvolvimento.')
    return redirect('usuarios:detalhes_usuario', usuario_id=usuario_id)

@login_required
@nivel_requerido(99)
def excluir_usuario_admin(request, usuario_id):
    """Excluir usuário como admin"""
    messages.info(request, 'Funcionalidade em desenvolvimento.')
    return redirect('usuarios:detalhes_usuario', usuario_id=usuario_id)

@login_required
@nivel_requerido(50)
def promover_usuario(request, usuario_id):
    """Promover usuário"""
    messages.info(request, 'Funcionalidade em desenvolvimento.')
    return redirect('usuarios:detalhes_usuario', usuario_id=usuario_id)

# ==================== SISTEMA ====================
@login_required
@nivel_requerido(99)
def sistema_status(request):
    """Status do sistema"""
    return render(request, 'usuarios/admin/sistema_status.html')

@login_required
@nivel_requerido(99)
def executar_manutencao(request):
    """Executar manutenção"""
    messages.info(request, 'Funcionalidade em desenvolvimento.')
    return redirect('usuarios:sistema_status')

# ==================== VIEW DE TESTE ====================
def testar_sistema(request):
    """Página de teste"""
    return render(request, 'usuarios/teste.html', {'status': 'Sistema funcionando!'})