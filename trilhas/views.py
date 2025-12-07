# trilhas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from .models import Trilha, Modulo, ProgressoTrilha

def index(request):
    """Lista todas as trilhas"""
    trilhas = Trilha.objects.filter(ativo=True).order_by('ordem')
    
    # Se o usuário estiver logado, mostrar progresso
    progressos = {}
    if request.user.is_authenticated:
        progressos = {
            p.trilha_id: p 
            for p in ProgressoTrilha.objects.filter(usuario=request.user)
        }
    
    return render(request, 'trilhas/index.html', {
        'trilhas': trilhas,
        'progressos': progressos
    })

@login_required
def detalhe(request, trilha_id):
    """Detalhes de uma trilha específica"""
    trilha = get_object_or_404(Trilha, id=trilha_id, ativo=True)
    modulos = trilha.modulos.all().order_by('ordem')
    
    # Obter ou criar progresso do usuário
    progresso, criado = ProgressoTrilha.objects.get_or_create(
        usuario=request.user,
        trilha=trilha,
        defaults={'modulo_atual': modulos.first() if modulos.exists() else None}
    )
    
    return render(request, 'trilhas/detalhe.html', {
        'trilha': trilha,
        'modulos': modulos,
        'progresso': progresso
    })

@login_required
def modulo_detalhe(request, trilha_id, modulo_id):
    """Detalhes de um módulo específico"""
    trilha = get_object_or_404(Trilha, id=trilha_id, ativo=True)
    modulo = get_object_or_404(Modulo, id=modulo_id, trilha=trilha)
    
    # Atualizar progresso
    progresso, criado = ProgressoTrilha.objects.get_or_create(
        usuario=request.user,
        trilha=trilha
    )
    progresso.modulo_atual = modulo
    progresso.save()
    
    # Calcular percentual concluído
    modulos_total = trilha.modulos.count()
    if modulos_total > 0:
        modulos_antes = trilha.modulos.filter(ordem__lt=modulo.ordem).count()
        progresso.percentual_concluido = (modulos_antes / modulos_total) * 100
        progresso.save()
    
    return render(request, 'trilhas/modulo.html', {
        'trilha': trilha,
        'modulo': modulo,
        'progresso': progresso
    })

@login_required
def iniciar_trilha(request, trilha_id):
    """Iniciar uma trilha"""
    trilha = get_object_or_404(Trilha, id=trilha_id, ativo=True)
    
    # Criar progresso se não existir
    progresso, criado = ProgressoTrilha.objects.get_or_create(
        usuario=request.user,
        trilha=trilha,
        defaults={'modulo_atual': trilha.modulos.first()}
    )
    
    return redirect('trilhas_detalhe', trilha_id=trilha.id)

@login_required
def marcar_concluido(request, modulo_id):
    """Marcar um módulo como concluído"""
    modulo = get_object_or_404(Modulo, id=modulo_id)
    trilha = modulo.trilha
    
    try:
        progresso = ProgressoTrilha.objects.get(
            usuario=request.user,
            trilha=trilha
        )
        
        # Marcar próximo módulo
        proximo_modulo = trilha.modulos.filter(ordem__gt=modulo.ordem).first()
        progresso.modulo_atual = proximo_modulo
        
        # Calcular percentual
        modulos_total = trilha.modulos.count()
        modulos_concluidos = trilha.modulos.filter(ordem__lte=modulo.ordem).count()
        
        if modulos_total > 0:
            progresso.percentual_concluido = (modulos_concluidos / modulos_total) * 100
            
            # Se concluiu todos os módulos
            if modulos_concluidos == modulos_total:
                progresso.concluido = True
                progresso.data_conclusao = timezone.now()
                
                # Adicionar pontos ao usuário
                request.user.pontos += trilha.pontos_recompensa
                request.user.save()
        
        progresso.save()
        
        messages.success(request, f'Módulo "{modulo.titulo}" concluído!')
        
        if proximo_modulo:
            return redirect('trilhas_modulo', trilha_id=trilha.id, modulo_id=proximo_modulo.id)
        else:
            return redirect('trilhas_detalhe', trilha_id=trilha.id)
            
    except ProgressoTrilha.DoesNotExist:
        messages.error(request, 'Você precisa iniciar a trilha primeiro.')
        return redirect('trilhas_detalhe', trilha_id=trilha.id)