# trilhas/views.py - VERSÃO FINAL COM SEU DESIGN
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def trilhas(request):
    """Página principal das trilhas - COM SEU DESIGN PRE/DOURADO"""
    return render(request, 'trilhas/trilhas.html')

def trilha_detalhe(request, nome_trilha):
    """Página detalhada de uma trilha"""
    # Informações básicas da trilha
    trilhas_info = {
        'python': {'nome': 'Python Fundamentals'},
        'javascript': {'nome': 'JavaScript Moderno'},
        'sql': {'nome': 'Banco de Dados SQL'},
        'web': {'nome': 'Desenvolvimento Web'},
        'algoritmos': {'nome': 'Algoritmos & Estruturas'},
        'datascience': {'nome': 'Data Science'},
    }
    
    trilha = trilhas_info.get(nome_trilha, {'nome': nome_trilha.title()})
    
    context = {
        'trilha': trilha,
        'nome_trilha': nome_trilha,
    }
    
    return render(request, 'trilhas/detalhe.html', context)