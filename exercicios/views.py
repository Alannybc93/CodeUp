# exercicios/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    """Página principal de exercícios"""
    # Dados de exemplo (substitua por dados reais do seu banco)
    exercicios = [
        {
            'id': 1,
            'titulo': 'Hello World em Python',
            'enunciado': 'Crie um programa que imprima "Hello, World!" na tela.',
            'dificuldade': 'facil',
            'pontos': 10,
            'modulo': {
                'titulo': 'Introdução ao Python',
                'trilha': {
                    'titulo': 'Python Fundamentals'
                }
            }
        },
        {
            'id': 2,
            'titulo': 'Calculadora Simples',
            'enunciado': 'Crie uma calculadora que some dois números fornecidos pelo usuário.',
            'dificuldade': 'facil',
            'pontos': 15,
            'modulo': {
                'titulo': 'Operadores e Entrada',
                'trilha': {
                    'titulo': 'Python Fundamentals'
                }
            }
        },
        {
            'id': 3,
            'titulo': 'Verificador de Números Primos',
            'enunciado': 'Escreva uma função que verifique se um número é primo.',
            'dificuldade': 'medio',
            'pontos': 25,
            'modulo': {
                'titulo': 'Estruturas de Controle',
                'trilha': {
                    'titulo': 'Python Fundamentals'
                }
            }
        },
        {
            'id': 4,
            'titulo': 'Ordenação de Lista',
            'enunciado': 'Implemente o algoritmo de ordenação bubble sort.',
            'dificuldade': 'medio',
            'pontos': 30,
            'modulo': {
                'titulo': 'Algoritmos Básicos',
                'trilha': {
                    'titulo': 'Algoritmos & Estruturas'
                }
            }
        },
        {
            'id': 5,
            'titulo': 'Manipulação de Arrays',
            'enunciado': 'Crie funções para manipular arrays em JavaScript.',
            'dificuldade': 'facil',
            'pontos': 12,
            'modulo': {
                'titulo': 'Arrays e Objetos',
                'trilha': {
                    'titulo': 'JavaScript Moderno'
                }
            }
        },
        {
            'id': 6,
            'titulo': 'Consulta SQL Complexa',
            'enunciado': 'Escreva uma consulta SQL para encontrar dados específicos.',
            'dificuldade': 'dificil',
            'pontos': 40,
            'modulo': {
                'titulo': 'Joins e Subqueries',
                'trilha': {
                    'titulo': 'Banco de Dados SQL'
                }
            }
        },
    ]
    
    # Filtros
    modulo_selecionado = request.GET.get('modulo', '')
    dificuldade_selecionada = request.GET.get('dificuldade', '')
    
    # Aplicar filtros
    if modulo_selecionado:
        exercicios = [e for e in exercicios if str(e.get('modulo_id', '')) == modulo_selecionado]
    
    if dificuldade_selecionada:
        exercicios = [e for e in exercicios if e['dificuldade'] == dificuldade_selecionada]
    
    # Módulos para o filtro
    modulos = [
        {'id': 1, 'titulo': 'Introdução ao Python', 'trilha': {'titulo': 'Python Fundamentals'}},
        {'id': 2, 'titulo': 'Operadores e Entrada', 'trilha': {'titulo': 'Python Fundamentals'}},
        {'id': 3, 'titulo': 'Estruturas de Controle', 'trilha': {'titulo': 'Python Fundamentals'}},
        {'id': 4, 'titulo': 'Algoritmos Básicos', 'trilha': {'titulo': 'Algoritmos & Estruturas'}},
        {'id': 5, 'titulo': 'Arrays e Objetos', 'trilha': {'titulo': 'JavaScript Moderno'}},
        {'id': 6, 'titulo': 'Joins e Subqueries', 'trilha': {'titulo': 'Banco de Dados SQL'}},
    ]
    
    context = {
        'exercicios': exercicios,
        'modulos': modulos,
        'selected_modulo': modulo_selecionado,
        'selected_dificuldade': dificuldade_selecionada,
        'user': request.user,
    }
    
    return render(request, 'exercicios/index.html', context)

@login_required
def meus_exercicios(request):
    """Exercícios do usuário"""
    # Em uma implementação real, você buscaria os exercícios do usuário do banco
    exercicios_resolvidos = []
    
    context = {
        'exercicios_resolvidos': exercicios_resolvidos,
        'user': request.user,
    }
    
    return render(request, 'exercicios/meus.html', context)

def detalhe(request, exercicio_id):
    """Detalhes de um exercício específico"""
    # Dados de exemplo (substitua por dados reais)
    exercicio = {
        'id': exercicio_id,
        'titulo': f'Exercício #{exercicio_id}',
        'enunciado': 'Descrição detalhada do exercício...',
        'dificuldade': 'medio',
        'pontos': 20,
        'modulo': {
            'titulo': 'Módulo de Exemplo',
            'trilha': {
                'titulo': 'Trilha de Exemplo'
            }
        },
        'exemplos': [
            'Exemplo de entrada: [1, 2, 3]',
            'Exemplo de saída: 6'
        ],
        'restricoes': [
            '0 <= n <= 100',
            'Use apenas loops for'
        ]
    }
    
    context = {
        'exercicio': exercicio,
        'user': request.user,
    }
    
    return render(request, 'exercicios/detalhe.html', context)

@login_required
def resolver(request, exercicio_id):
    """Resolver um exercício"""
    # Dados de exemplo
    exercicio = {
        'id': exercicio_id,
        'titulo': f'Exercício #{exercicio_id}',
        'enunciado': 'Escreva uma função que resolva o problema descrito abaixo.',
        'linguagens': ['python', 'javascript', 'java'],
        'testes': [
            {'entrada': '5', 'saida': '25'},
            {'entrada': '10', 'saida': '100'}
        ]
    }
    
    if request.method == 'POST':
        # Aqui você processaria a solução enviada
        codigo = request.POST.get('codigo', '')
        linguagem = request.POST.get('linguagem', 'python')
        
        # Simular processamento
        messages.success(request, 'Solução enviada com sucesso! Em breve você terá o resultado.')
        return render(request, 'exercicios/resultado.html', {
            'exercicio': exercicio,
            'user': request.user,
            'sucesso': True
        })
    
    context = {
        'exercicio': exercicio,
        'user': request.user,
    }
    
    return render(request, 'exercicios/resolver.html', context)