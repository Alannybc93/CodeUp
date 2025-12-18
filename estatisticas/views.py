# estatisticas/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum, Avg, Q
from django.utils import timezone
from datetime import timedelta
from usuarios.models import Usuario
from trilhas.models import ProgressoTrilha, ProgressoModulo
from exercicios.models import Submissao, Exercicio
from django.core.exceptions import ObjectDoesNotExist

@login_required
def dashboard_estatisticas(request):
    usuario = request.user
    
    # Estatísticas gerais
    estatisticas = {
        'total_exercicios': Submissao.objects.filter(usuario=usuario).count(),
        'exercicios_corretos': Submissao.objects.filter(usuario=usuario, status='CORRETO').count(),
        'taxa_acerto': calcular_taxa_acerto(usuario),
        'total_trilhas': ProgressoTrilha.objects.filter(usuario=usuario).count(),
        'trilhas_concluidas': ProgressoTrilha.objects.filter(usuario=usuario, concluida=True).count(),
        'tempo_total_estudo': calcular_tempo_estudo(usuario),
    }
    
    # Progresso por dia (últimos 30 dias)
    progresso_diario = calcular_progresso_diario(usuario, 30)
    
    # Distribuição por dificuldade
    distribuicao_dificuldade = calcular_distribuicao_dificuldade(usuario)
    
    # Trilhas em progresso
    trilhas_progresso = ProgressoTrilha.objects.filter(
        usuario=usuario,
        concluida=False
    ).select_related('trilha').order_by('-ultimo_acesso')[:5]
    
    context = {
        'estatisticas': estatisticas,
        'progresso_diario': progresso_diario,
        'distribuicao_dificuldade': distribuicao_dificuldade,
        'trilhas_progresso': trilhas_progresso,
    }
    
    if request.user.tipo == 'PROFESSOR':
        context.update(dashboard_professor(request))
    
    return render(request, 'estatisticas/dashboard.html', context)

def calcular_taxa_acerto(usuario):
    total = Submissao.objects.filter(usuario=usuario).count()
    if total == 0:
        return 0
    corretos = Submissao.objects.filter(usuario=usuario, status='CORRETO').count()
    return round((corretos / total) * 100, 1)

def calcular_tempo_estudo(usuario):
    """Calcula o tempo total de estudo em minutos"""
    tempo_segundos = ProgressoModulo.objects.filter(
        usuario=usuario,
        concluido=True
    ).aggregate(total=Sum('tempo_gasto'))['total']
    
    if tempo_segundos is None:
        return 0
    
    # Converter segundos para minutos
    tempo_minutos = tempo_segundos / 60
    
    # Formatar: se for mais de 60 minutos, converter para horas
    if tempo_minutos >= 60:
        horas = int(tempo_minutos // 60)
        minutos = int(tempo_minutos % 60)
        return f"{horas}h {minutos}min"
    else:
        return f"{int(tempo_minutos)} min"

def calcular_progresso_diario(usuario, dias=30):
    """Calcula progresso diário dos últimos N dias"""
    from django.db.models.functions import TruncDate
    
    data_inicio = timezone.now() - timedelta(days=dias)
    
    progresso = Submissao.objects.filter(
        usuario=usuario,
        data_submissao__gte=data_inicio
    ).annotate(
        data=TruncDate('data_submissao')
    ).values('data').annotate(
        total=Count('id'),
        corretos=Count('id', filter=Q(status='CORRETO'))
    ).order_by('data')
    
    return list(progresso)

def calcular_distribuicao_dificuldade(usuario):
    """Calcula distribuição de exercícios por dificuldade"""
    distribuicao = Submissao.objects.filter(
        usuario=usuario
    ).values(
        'exercicio__dificuldade'
    ).annotate(
        total=Count('id'),
        corretos=Count('id', filter=Q(status='CORRETO'))
    ).order_by('exercicio__dificuldade')
    
    resultado = {}
    for item in distribuicao:
        dificuldade = item['exercicio__dificuldade']
        if dificuldade:
            resultado[dificuldade] = {
                'total': item['total'],
                'corretos': item['corretos'],
                'taxa_acerto': round((item['corretos'] / item['total']) * 100, 1) if item['total'] > 0 else 0
            }
    
    return resultado

def dashboard_professor(request):
    """Estatísticas específicas para professores"""
    if request.user.tipo != 'PROFESSOR':
        return {}
    
    professor = request.user
    
    # Estatísticas para professores
    total_alunos = Usuario.objects.filter(tipo='ALUNO').count()
    total_exercicios_criados = Exercicio.objects.filter(criador=professor).count()
    
    # Trilhas criadas pelo professor
    from trilhas.models import Trilha
    trilhas_criadas = Trilha.objects.filter(criador=professor)
    
    # Progresso médio dos alunos nas trilhas do professor
    progresso_alunos = []
    for trilha in trilhas_criadas:
        progressos = ProgressoTrilha.objects.filter(trilha=trilha)
        if progressos.exists():
            media_progresso = progressos.aggregate(Avg('percentual_conclusao'))['percentual_conclusao__avg']
            progresso_alunos.append({
                'trilha': trilha,
                'media_progresso': round(media_progresso, 1) if media_progresso else 0,
                'total_alunos': progressos.count(),
            })
    
    return {
        'total_alunos': total_alunos,
        'total_exercicios_criados': total_exercicios_criados,
        'trilhas_criadas': trilhas_criadas,
        'progresso_alunos': progresso_alunos,
    }