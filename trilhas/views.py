# trilhas/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def trilhas(request):
    """Página principal das trilhas"""
    # Dados das trilhas (agora mais completos)
    trilhas_disponiveis = [
        {
            'id': 1,
            'nome': 'Python Fundamentals',
            'descricao': 'Aprenda Python do zero: sintaxe, estruturas de dados, funções, orientação a objetos e muito mais. Ideal para iniciantes.',
            'icone': 'fab fa-python',
            'url': 'trilhas:trilha_python',
            'progresso': 75 if request.user.is_authenticated else 0,
            'modulos': 25,
            'horas': 40,
            'dificuldade': 'Iniciante',
            'cor': '#306998',
            'alunos': '2.5k',
        },
        {
            'id': 2,
            'nome': 'JavaScript Moderno',
            'descricao': 'Domine JavaScript ES6+, manipulação do DOM, async/await, e prepare-se para frameworks modernos.',
            'icone': 'fab fa-js-square',
            'url': 'trilhas:trilha_javascript',
            'progresso': 30 if request.user.is_authenticated else 0,
            'modulos': 30,
            'horas': 50,
            'dificuldade': 'Intermediário',
            'cor': '#F0DB4F',
            'alunos': '1.8k',
        },
        {
            'id': 3,
            'nome': 'Banco de Dados SQL',
            'descricao': 'Comandos SQL, modelagem de dados, consultas complexas, otimização e práticas recomendadas.',
            'icone': 'fas fa-database',
            'url': 'trilhas:trilha_sql',
            'progresso': 10 if request.user.is_authenticated else 0,
            'modulos': 20,
            'horas': 35,
            'dificuldade': 'Iniciante',
            'cor': '#00758F',
            'alunos': '1.2k',
        },
        {
            'id': 4,
            'nome': 'Desenvolvimento Web',
            'descricao': 'HTML5, CSS3, JavaScript, responsividade, frameworks front-end e back-end para criar aplicações web completas.',
            'icone': 'fas fa-globe',
            'url': 'trilhas:trilha_web',
            'progresso': 0,
            'modulos': 35,
            'horas': 60,
            'dificuldade': 'Intermediário',
            'cor': '#E44D26',
            'alunos': '3.2k',
        },
        {
            'id': 5,
            'nome': 'Algoritmos & Estruturas',
            'descricao': 'Fundamentos de algoritmos, estruturas de dados, complexidade, e resolução de problemas para entrevistas técnicas.',
            'icone': 'fas fa-brain',
            'url': 'trilhas:trilha_algoritmos',
            'progresso': 0,
            'modulos': 28,
            'horas': 45,
            'dificuldade': 'Intermediário',
            'cor': '#8A2BE2',
            'alunos': '1.5k',
        },
        {
            'id': 6,
            'nome': 'Data Science',
            'descricao': 'Análise de dados, visualização, machine learning básico e bibliotecas como Pandas, NumPy e Matplotlib.',
            'icone': 'fas fa-chart-bar',
            'url': 'trilhas:trilha_datascience',
            'progresso': 0,
            'modulos': 32,
            'horas': 55,
            'dificuldade': 'Avançado',
            'cor': '#1F77B4',
            'alunos': '1.1k',
        },
    ]
    
    context = {
        'trilhas': trilhas_disponiveis,
        'usuario': request.user,
        'total_trilhas': len(trilhas_disponiveis),
    }
    
    return render(request, 'trilhas/trilhas.html', context)

def trilha_detalhe(request, nome_trilha):
    """Detalhes de uma trilha específica"""
    # Mapeamento de informações das trilhas
    trilhas_info = {
        'python': {
            'nome': 'Python Fundamentals',
            'descricao': 'Aprenda Python desde os conceitos básicos até a criação de aplicações reais.',
            'icone': 'fab fa-python',
            'cor': '#306998',
            'modulos': 25,
            'horas': 40,
            'dificuldade': 'Iniciante',
        },
        'javascript': {
            'nome': 'JavaScript Moderno',
            'descricao': 'Domine JavaScript moderno e todas as funcionalidades do ES6+.',
            'icone': 'fab fa-js-square',
            'cor': '#F0DB4F',
            'modulos': 30,
            'horas': 50,
            'dificuldade': 'Intermediário',
        },
        'sql': {
            'nome': 'Banco de Dados SQL',
            'descricao': 'Aprenda SQL desde consultas básicas até otimização de bancos de dados.',
            'icone': 'fas fa-database',
            'cor': '#00758F',
            'modulos': 20,
            'horas': 35,
            'dificuldade': 'Iniciante',
        },
        'web': {
            'nome': 'Desenvolvimento Web',
            'descricao': 'Crie sites responsivos e modernos usando as tecnologias mais atuais.',
            'icone': 'fas fa-globe',
            'cor': '#E44D26',
            'modulos': 35,
            'horas': 60,
            'dificuldade': 'Intermediário',
        },
        'algoritmos': {
            'nome': 'Algoritmos & Estruturas',
            'descricao': 'Desenvolva sua lógica de programação com algoritmos clássicos.',
            'icone': 'fas fa-brain',
            'cor': '#8A2BE2',
            'modulos': 28,
            'horas': 45,
            'dificuldade': 'Intermediário',
        },
        'datascience': {
            'nome': 'Data Science',
            'descricao': 'Análise de dados, estatística e machine learning com Python.',
            'icone': 'fas fa-chart-bar',
            'cor': '#1F77B4',
            'modulos': 32,
            'horas': 55,
            'dificuldade': 'Avançado',
        },
    }
    
    # Obtém informações da trilha ou usa valores padrão
    trilha_info = trilhas_info.get(nome_trilha, {
        'nome': nome_trilha.title(),
        'descricao': 'Trilha de aprendizado em desenvolvimento.',
        'icone': 'fas fa-road',
        'cor': '#FFD700',
        'modulos': 0,
        'horas': 0,
        'dificuldade': 'Em breve',
    })
    
    context = {
        'trilha': trilha_info,
        'nome_trilha': nome_trilha,
        'usuario': request.user,
    }
    
    return render(request, 'trilhas/detalhe.html', context)