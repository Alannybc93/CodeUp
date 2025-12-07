# exercicios/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Exercicio
from trilhas.models import Modulo

def index(request):
    """Lista todos os exercícios"""
    exercicios = Exercicio.objects.all().select_related('modulo', 'modulo__trilha')
    modulos = Modulo.objects.all()
    
    # Filtrar por módulo se especificado
    modulo_id = request.GET.get('modulo')
    if modulo_id:
        exercicios = exercicios.filter(modulo_id=modulo_id)
    
    # Filtrar por dificuldade se especificado
    dificuldade = request.GET.get('dificuldade')
    if dificuldade:
        exercicios = exercicios.filter(dificuldade=dificuldade)
    
    return render(request, 'exercicios/index.html', {
        'exercicios': exercicios,
        'modulos': modulos,
        'selected_modulo': modulo_id,
        'selected_dificuldade': dificuldade
    })

@login_required
def detalhe(request, exercicio_id):
    """Detalhes de um exercício específico"""
    exercicio = get_object_or_404(Exercicio, id=exercicio_id)
    
    # Verificar se o usuário já resolveu este exercício
    resolvido = False
    if hasattr(request.user, 'exercicios_resolvidos'):
        resolvido = exercicio in request.user.exercicios_resolvidos.all()
    
    return render(request, 'exercicios/detalhe.html', {
        'exercicio': exercicio,
        'resolvido': resolvido
    })

@login_required
def resolver(request, exercicio_id):
    """Página para resolver o exercício"""
    exercicio = get_object_or_404(Exercicio, id=exercicio_id)
    
    if request.method == 'POST':
        codigo_usuario = request.POST.get('codigo', '')
        
        # Verificação básica da resposta
        # Em um sistema real, isso seria mais complexo
        resposta_simplificada = exercicio.resposta_correta.strip().lower().replace(' ', '')
        usuario_simplificado = codigo_usuario.strip().lower().replace(' ', '')
        
        # Verificação aproximada (para demonstração)
        if usuario_simplificado in resposta_simplificada or resposta_simplificada in usuario_simplificado:
            # Marcar como resolvido
            if not hasattr(request.user, 'exercicios_resolvidos'):
                # Criar relação se não existir
                request.user.exercicios_resolvidos.add(exercicio)
            else:
                request.user.exercicios_resolvidos.add(exercicio)
            
            # Adicionar pontos
            request.user.pontos += exercicio.pontos
            request.user.save()
            
            messages.success(request, f'Parabéns! Exercício resolvido! +{exercicio.pontos} pontos!')
            return redirect('exercicios_detalhe', exercicio_id=exercicio.id)
        else:
            messages.error(request, 'Resposta incorreta. Tente novamente!')
    
    return render(request, 'exercicios/resolver.html', {
        'exercicio': exercicio
    })

@login_required
def meus_exercicios(request):
    """Exercícios resolvidos pelo usuário"""
    if hasattr(request.user, 'exercicios_resolvidos'):
        exercicios = request.user.exercicios_resolvidos.all()
    else:
        exercicios = []
    
    return render(request, 'exercicios/meus.html', {
        'exercicios': exercicios
    })