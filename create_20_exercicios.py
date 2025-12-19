import os
import django
import sys

# Adicione o diretório do projeto ao path se necessário
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeup.settings')
django.setup()

from exercicios.models import Exercicio
from trilhas.models import Trilha, Modulo

def criar_questoes():
    print("Criando 20 questões...")

    # Criar trilha e módulo se não existirem
    trilha, _ = Trilha.objects.get_or_create(
        titulo="Python para Iniciantes",
        defaults={
            'descricao': 'Domine Python com exercícios práticos',   
            'icone': 'fas fa-code',
            'ordem': 1
        }
    )

    modulo, _ = Modulo.objects.get_or_create(
        trilha=trilha,
        titulo="Fundamentos da Programação",
        defaults={
            'descricao': 'Conceitos básicos de programação com Python',
            'ordem': 1
        }
    )

    # Lista de 20 questões - SEM os campos dica e explicacao
    questoes = [
        {
            'titulo': 'Hello World em Python',
            'enunciado': 'Escreva um programa que imprima "Hello, World!" na tela.',
            'codigo_inicial': '# Escreva seu código aqui\n',        
            'resposta_correta': 'print("Hello, World!")',
            'pontos': 10,
            'dificuldade': 'iniciante'
        },
        {
            'titulo': 'Soma de dois números',
            'enunciado': 'Crie uma função chamada soma que receba dois números e retorne a soma deles.',
            'codigo_inicial': 'def soma(a, b):\n    # Complete a função\n    pass',
            'resposta_correta': 'def soma(a, b):\n    return a + b',
            'pontos': 15,
            'dificuldade': 'iniciante'
        },
        {
            'titulo': 'Variável e Atribuição',
            'enunciado': 'Crie uma variável chamada "nome" e atribua seu nome a ela, depois imprima.',
            'codigo_inicial': '# Crie a variável nome\n\n# Imprima a variável',
            'resposta_correta': 'nome = "Seu Nome"\nprint(nome)',   
            'pontos': 10,
            'dificuldade': 'iniciante'
        },
        {
            'titulo': 'Condição Simples',
            'enunciado': 'Verifique se um número é positivo. Retorne True se for positivo, False caso contrário.',
            'codigo_inicial': 'def eh_positivo(numero):\n    # Complete a função\n    pass',
            'resposta_correta': 'def eh_positivo(numero):\n    return numero > 0',
            'pontos': 15,
            'dificuldade': 'iniciante'
        },
        {
            'titulo': 'Lista Básica',
            'enunciado': 'Crie uma lista com os números de 1 a 5 e imprima o terceiro elemento.',
            'codigo_inicial': '# Crie a lista\n\n# Imprima o terceiro elemento',
            'resposta_correta': 'numeros = [1, 2, 3, 4, 5]\nprint(numeros[2])',
            'pontos': 12,
            'dificuldade': 'iniciante'
        },
        {
            'titulo': 'Função com Múltiplos Parâmetros',
            'enunciado': 'Crie uma função que calcule a média de três números.',
            'codigo_inicial': 'def calcular_media(a, b, c):\n    # Complete a função\n    pass',
            'resposta_correta': 'def calcular_media(a, b, c):\n    return (a + b + c) / 3',
            'pontos': 20,
            'dificuldade': 'basico'
        },
        {
            'titulo': 'Loop For Simples',
            'enunciado': 'Use um loop for para imprimir os números de 1 a 10.',
            'codigo_inicial': '# Use um loop for\n',
            'resposta_correta': 'for i in range(1, 11):\n    print(i)',
            'pontos': 18,
            'dificuldade': 'basico'
        },
        {
            'titulo': 'Verificar Número Par',
            'enunciado': 'Escreva uma função que retorne True se um número for par, False se for ímpar.',
            'codigo_inicial': 'def eh_par(numero):\n    # Complete a função\n    pass',
            'resposta_correta': 'def eh_par(numero):\n    return numero % 2 == 0',
            'pontos': 20,
            'dificuldade': 'basico'
        },
        {
            'titulo': 'Contar Caracteres',
            'enunciado': 'Escreva uma função que conte quantos caracteres tem em uma string.',
            'codigo_inicial': 'def contar_caracteres(texto):\n    # Complete a função\n    pass',
            'resposta_correta': 'def contar_caracteres(texto):\n    return len(texto)',
            'pontos': 15,
            'dificuldade': 'basico'
        },
        {
            'titulo': 'Dicionário Básico',
            'enunciado': 'Crie um dicionário com seu nome e idade, depois acesse a idade.',
            'codigo_inicial': '# Crie o dicionário\n\n# Acesse a idade',
            'resposta_correta': 'pessoa = {"nome": "Seu Nome", "idade": 25}\nprint(pessoa["idade"])',
            'pontos': 18,
            'dificuldade': 'basico'
        },
        {
            'titulo': 'Fatorial com Recursão',
            'enunciado': 'Implemente uma função recursiva para calcular o fatorial de um número.',
            'codigo_inicial': 'def fatorial(n):\n    # Complete a função recursiva\n    pass',
            'resposta_correta': 'def fatorial(n):\n    if n == 0 or n == 1:\n        return 1\n    else:\n        return n * fatorial(n-1)',
            'pontos': 30,
            'dificuldade': 'intermediario'
        },
        {
            'titulo': 'Palíndromo',
            'enunciado': 'Verifique se uma string é um palíndromo (lê-se igual de trás para frente).',
            'codigo_inicial': 'def eh_palindromo(texto):\n    # Complete a função\n    pass',
            'resposta_correta': 'def eh_palindromo(texto):\n    texto = texto.lower().replace(" ", "")\n    return texto == texto[::-1]',  
            'pontos': 25,
            'dificuldade': 'intermediario'
        },
        {
            'titulo': 'Encontrar Maior Número',
            'enunciado': 'Encontre o maior número em uma lista sem usar a função max().',
            'codigo_inicial': 'def maior_numero(lista):\n    # Complete a função\n    pass',
            'resposta_correta': 'def maior_numero(lista):\n    maior = lista[0]\n    for num in lista:\n        if num > maior:\n          maior = num\n    return maior',
            'pontos': 25,
            'dificuldade': 'intermediario'
        },
        {
            'titulo': 'Contar Vogais',
            'enunciado': 'Conte quantas vogais existem em uma string.',
            'codigo_inicial': 'def contar_vogais(texto):\n    # Complete a função\n    pass',
            'resposta_correta': 'def contar_vogais(texto):\n    vogais = "aeiouAEIOU"\n    contador = 0\n    for char in texto:\n        if char in vogais:\n            contador += 1\n    return contador',     
            'pontos': 22,
            'dificuldade': 'intermediario'
        },
        {
            'titulo': 'Ordenar Lista',
            'enunciado': 'Ordene uma lista de números em ordem crescente sem usar sort().',
            'codigo_inicial': 'def ordenar_lista(lista):\n    # Implemente sua própria ordenação\n    pass',
            'resposta_correta': 'def ordenar_lista(lista):\n    for i in range(len(lista)):\n        for j in range(i+1, len(lista)):\n            if lista[i] > lista[j]:\n                lista[i], lista[j] = lista[j], lista[i]\n    return lista',
            'pontos': 35,
            'dificuldade': 'intermediario'
        },
        {
            'titulo': 'Sequência de Fibonacci',
            'enunciado': 'Gere os primeiros n números da sequência de Fibonacci.',
            'codigo_inicial': 'def fibonacci(n):\n    # Complete a função\n    pass',
            'resposta_correta': '''def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq''',
            'pontos': 40,
            'dificuldade': 'avancado'
        },
        {
            'titulo': 'Validador de CPF',
            'enunciado': 'Implemente uma função que valide um CPF brasileiro.',
            'codigo_inicial': 'def validar_cpf(cpf):\n    # Complete a função\n    pass',
            'resposta_correta': '''def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    # Primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    if digito1 != int(cpf[9]):
        return False

    # Segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    return digito2 == int(cpf[10])''',
            'pontos': 50,
            'dificuldade': 'avancado'
        },
        {
            'titulo': 'Conversor Decimal para Binário',
            'enunciado': 'Converta um número decimal para binário sem usar funções pré-definidas.',
            'codigo_inicial': 'def decimal_para_binario(n):\n    # Complete a função\n    pass',
            'resposta_correta': '''def decimal_para_binario(n):     
    if n == 0:
        return "0"

    binario = ""
    while n > 0:
        resto = n % 2
        binario = str(resto) + binario
        n = n // 2

    return binario''',
            'pontos': 35,
            'dificuldade': 'avancado'
        },
        {
            'titulo': 'Jogo da Velha - Verificar Vencedor',
            'enunciado': 'Dada uma matriz 3x3 do jogo da velha, verifique se há um vencedor.',
            'codigo_inicial': '''def verificar_vencedor(tabuleiro): 
    # Complete a função
    pass''',
            'resposta_correta': '''def verificar_vencedor(tabuleiro):
    # Verificar linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != "":
            return tabuleiro[i][0]

    # Verificar colunas
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j] != "":
            return tabuleiro[0][j]

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "": 
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "": 
        return tabuleiro[0][2]

    return None''',
            'pontos': 60,
            'dificuldade': 'expert'
        },
        {
            'titulo': 'Cifra de César',
            'enunciado': 'Implemente a cifra de César para criptografar e descriptografar textos.',
            'codigo_inicial': '''def cifra_cesar(texto, deslocamento, modo='criptografar'):
    # Complete a função
    pass''',
            'resposta_correta': '''def cifra_cesar(texto, deslocamento, modo='criptografar'):
    resultado = ""

    if modo == 'descriptografar':
        deslocamento = -deslocamento

    for char in texto:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            codigo = ord(char) - ascii_offset
            novo_codigo = (codigo + deslocamento) % 26
            resultado += chr(novo_codigo + ascii_offset)
        else:
            resultado += char

    return resultado''',
            'pontos': 55,
            'dificuldade': 'expert'
        }
    ]

    # Criar os exercícios
    for i, questao in enumerate(questoes, 1):
        try:
            exercicio, created = Exercicio.objects.get_or_create(       
                modulo=modulo,
                titulo=questao['titulo'],
                defaults={
                    'enunciado': questao['enunciado'],
                    'codigo_inicial': questao['codigo_inicial'],        
                    'resposta_correta': questao['resposta_correta'],    
                    'pontos': questao['pontos'],
                    'dificuldade': questao['dificuldade']
                }
            )

            if created:
                print(f"{i}. Criado: {questao['titulo']} ({questao['dificuldade']}) - {questao['pontos']} pts")
            else:
                print(f"{i}. Já existe: {questao['titulo']}")
        except Exception as e:
            print(f"{i}. Erro ao criar '{questao['titulo']}': {e}")

    print(f"\nTotal: {len(questoes)} questões processadas!")
    print(f"Trilha: {trilha.titulo}")
    print(f"Módulo: {modulo.titulo}")

if __name__ == "__main__":
    criar_questoes()
