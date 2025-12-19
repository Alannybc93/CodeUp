from django.core.management.base import BaseCommand
from exercicios.models import Exercicio

class Command(BaseCommand):
    help = 'Popula o banco de dados com exercícios de exemplo'
    
    def handle(self, *args, **kwargs):
        exercicios = [
            # ========== PYTHON - FÁCIL ==========
            {
                'titulo': 'Hello World em Python',
                'descricao': 'Escreva um programa que imprima "Hello, World!" na tela.',
                'codigo_inicial': '# Seu código aqui',
                'solucao': 'print("Hello, World!")',
                'linguagem': 'python',
                'dificuldade': 'Fácil',
                'pontos': 10,
                'dica': 'Use a função print()',
                'explicacao': 'Em Python, usamos a função print() para exibir texto na tela.',
                'categoria': 'Introdução'
            },
            {
                'titulo': 'Soma de Dois Números',
                'descricao': 'Escreva uma função que receba dois números e retorne a soma deles.',
                'codigo_inicial': 'def soma(a, b):\n    # Complete a função',
                'solucao': 'def soma(a, b):\n    return a + b',
                'linguagem': 'python',
                'dificuldade': 'Fácil',
                'pontos': 15,
                'dica': 'Use o operador + para somar',
                'explicacao': 'A função recebe dois parâmetros e retorna a soma usando o operador +.',
                'categoria': 'Funções'
            },
            {
                'titulo': 'Verificar Número Par',
                'descricao': 'Escreva uma função que verifique se um número é par.',
                'codigo_inicial': 'def eh_par(numero):\n    # Complete a função',
                'solucao': 'def eh_par(numero):\n    return numero % 2 == 0',
                'linguagem': 'python',
                'dificuldade': 'Fácil',
                'pontos': 15,
                'dica': 'Use o operador módulo %',
                'explicacao': 'Um número é par se o resto da divisão por 2 for igual a zero.',
                'categoria': 'Lógica'
            },
            
            # ========== PYTHON - MÉDIO ==========
            {
                'titulo': 'Fatorial de um Número',
                'descricao': 'Escreva uma função que calcule o fatorial de um número (n!).',
                'codigo_inicial': 'def fatorial(n):\n    # Complete a função',
                'solucao': 'def fatorial(n):\n    resultado = 1\n    for i in range(1, n + 1):\n        resultado *= i\n    return resultado',
                'linguagem': 'python',
                'dificuldade': 'Médio',
                'pontos': 25,
                'dica': 'Use um loop for para multiplicar os números de 1 até n',
                'explicacao': 'O fatorial de n é o produto de todos os números inteiros de 1 até n.',
                'categoria': 'Matemática'
            },
            {
                'titulo': 'Contar Vogais em uma String',
                'descricao': 'Escreva uma função que conte quantas vogais existem em uma string.',
                'codigo_inicial': 'def contar_vogais(texto):\n    # Complete a função',
                'solucao': 'def contar_vogais(texto):\n    vogais = "aeiouAEIOU"\n    count = 0\n    for char in texto:\n        if char in vogais:\n            count += 1\n    return count',
                'linguagem': 'python',
                'dificuldade': 'Médio',
                'pontos': 20,
                'dica': 'Crie uma string com todas as vogais e verifique cada caractere',
                'explicacao': 'Iteramos sobre cada caractere da string e verificamos se está na lista de vogais.',
                'categoria': 'Strings'
            },
            {
                'titulo': 'Inverter uma Lista',
                'descricao': 'Escreva uma função que inverta os elementos de uma lista.',
                'codigo_inicial': 'def inverter_lista(lista):\n    # Complete a função',
                'solucao': 'def inverter_lista(lista):\n    return lista[::-1]',
                'linguagem': 'python',
                'dificuldade': 'Médio',
                'pontos': 20,
                'dica': 'Use slicing com passo negativo',
                'explicacao': 'Em Python, podemos usar lista[::-1] para criar uma cópia invertida da lista.',
                'categoria': 'Listas'
            },
            
            # ========== PYTHON - DIFÍCIL ==========
            {
                'titulo': 'Verificar Palíndromo',
                'descricao': 'Escreva uma função que verifique se uma string é um palíndromo (lê-se igual de trás para frente).',
                'codigo_inicial': 'def eh_palindromo(texto):\n    # Complete a função',
                'solucao': 'def eh_palindromo(texto):\n    texto = texto.lower().replace(" ", "")\n    return texto == texto[::-1]',
                'linguagem': 'python',
                'dificuldade': 'Difícil',
                'pontos': 30,
                'dica': 'Converta para minúsculas, remova espaços e compare com sua versão invertida',
                'explicacao': 'Um palíndromo permanece o mesmo quando invertido, após remover espaços e normalizar o caso.',
                'categoria': 'Algoritmos'
            },
            {
                'titulo': 'Ordenar Lista (Bubble Sort)',
                'descricao': 'Implemente o algoritmo Bubble Sort para ordenar uma lista de números.',
                'codigo_inicial': 'def bubble_sort(lista):\n    # Implemente o Bubble Sort',
                'solucao': 'def bubble_sort(lista):\n    n = len(lista)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if lista[j] > lista[j+1]:\n                lista[j], lista[j+1] = lista[j+1], lista[j]\n    return lista',
                'linguagem': 'python',
                'dificuldade': 'Difícil',
                'pontos': 35,
                'dica': 'Use dois loops aninhados para comparar elementos adjacentes',
                'explicacao': 'Bubble Sort compara elementos adjacentes e os troca se estiverem na ordem errada.',
                'categoria': 'Algoritmos'
            },
            
            # ========== JAVASCRIPT ==========
            {
                'titulo': 'Hello World em JavaScript',
                'descricao': 'Escreva um código JavaScript que imprima "Hello, World!" no console.',
                'codigo_inicial': '// Seu código aqui',
                'solucao': 'console.log("Hello, World!");',
                'linguagem': 'javascript',
                'dificuldade': 'Fácil',
                'pontos': 10,
                'dica': 'Use console.log()',
                'explicacao': 'Em JavaScript, usamos console.log() para imprimir no console do navegador.',
                'categoria': 'Introdução'
            },
            {
                'titulo': 'Função Soma em JavaScript',
                'descricao': 'Escreva uma função JavaScript que some dois números.',
                'codigo_inicial': 'function soma(a, b) {\n    // Complete a função\n}',
                'solucao': 'function soma(a, b) {\n    return a + b;\n}',
                'linguagem': 'javascript',
                'dificuldade': 'Fácil',
                'pontos': 15,
                'dica': 'Use o operador +',
                'explicacao': 'A sintaxe de função em JavaScript usa a palavra-chave function.',
                'categoria': 'Funções'
            },
            
            # ========== HTML/CSS ==========
            {
                'titulo': 'Criar Página HTML Básica',
                'descricao': 'Crie uma estrutura HTML básica com título e parágrafo.',
                'codigo_inicial': '<!DOCTYPE html>\n<html>\n<head>\n    <!-- Complete o código -->\n</head>\n<body>\n    <!-- Complete o código -->\n</body>\n</html>',
                'solucao': '<!DOCTYPE html>\n<html>\n<head>\n    <title>Minha Página</title>\n</head>\n<body>\n    <h1>Olá, Mundo!</h1>\n    <p>Esta é minha primeira página HTML.</p>\n</body>\n</html>',
                'linguagem': 'html',
                'dificuldade': 'Fácil',
                'pontos': 10,
                'dica': 'Use as tags h1 para título e p para parágrafo',
                'explicacao': 'HTML usa tags para estruturar o conteúdo. <h1> para títulos principais, <p> para parágrafos.',
                'categoria': 'Web'
            },
            {
                'titulo': 'Estilizar Botão com CSS',
                'descricao': 'Crie um botão estilizado com CSS que tenha fundo azul e texto branco.',
                'codigo_inicial': '<button class="meu-botao">Clique Aqui</button>\n<style>\n    .meu-botao {\n        /* Adicione estilos aqui */\n    }\n</style>',
                'solucao': '<button class="meu-botao">Clique Aqui</button>\n<style>\n    .meu-botao {\n        background-color: blue;\n        color: white;\n        padding: 10px 20px;\n        border: none;\n        border-radius: 5px;\n        cursor: pointer;\n    }\n</style>',
                'linguagem': 'css',
                'dificuldade': 'Médio',
                'pontos': 20,
                'dica': 'Use background-color para cor de fundo e color para cor do texto',
                'explicacao': 'CSS permite estilizar elementos HTML usando propriedades como background-color, color, padding, etc.',
                'categoria': 'Web'
            },
            
            # ========== JAVA ==========
            {
                'titulo': 'Hello World em Java',
                'descricao': 'Escreva um programa Java que imprima "Hello, World!"',
                'codigo_inicial': 'public class HelloWorld {\n    public static void main(String[] args) {\n        // Seu código aqui\n    }\n}',
                'solucao': 'public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}',
                'linguagem': 'java',
                'dificuldade': 'Médio',
                'pontos': 20,
                'dica': 'Use System.out.println()',
                'explicacao': 'Em Java, a estrutura básica requer uma classe e o método main. Usamos System.out.println() para imprimir.',
                'categoria': 'Introdução'
            },
            
            # ========== DESAFIOS EXTRAS ==========
            {
                'titulo': 'Jogo da Velha - Verificar Vencedor',
                'descricao': 'Escreva uma função que receba uma matriz 3x3 representando um jogo da velha e retorne o vencedor ("X", "O") ou None se não houver vencedor.',
                'codigo_inicial': 'def verificar_vencedor(tabuleiro):\n    # Implemente a função\n    pass',
                'solucao': 'def verificar_vencedor(tabuleiro):\n    # Verificar linhas\n    for i in range(3):\n        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":\n            return tabuleiro[i][0]\n    # Verificar colunas\n    for i in range(3):\n        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":\n            return tabuleiro[0][i]\n    # Verificar diagonais\n    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":\n        return tabuleiro[0][0]\n    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":\n        return tabuleiro[0][2]\n    return None',
                'linguagem': 'python',
                'dificuldade': 'Difícil',
                'pontos': 50,
                'categoria': 'Desafio',
                'dica': 'Verifique linhas, colunas e diagonais',
                'explicacao': 'Precisamos verificar todas as possíveis combinações vencedoras em um jogo da velha.',
            },
            {
                'titulo': 'Calculadora de Troco',
                'descricao': 'Escreva uma função que calcule o troco mínimo em notas/moedas para um valor dado.',
                'codigo_inicial': 'def calcular_troco(valor):\n    notas = [100, 50, 20, 10, 5, 2, 1]\n    # Complete a função',
                'solucao': 'def calcular_troco(valor):\n    notas = [100, 50, 20, 10, 5, 2, 1]\n    resultado = {}\n    for nota in notas:\n        if valor >= nota:\n            quantidade = valor // nota\n            resultado[nota] = quantidade\n            valor -= quantidade * nota\n    return resultado',
                'linguagem': 'python',
                'dificuldade': 'Médio',
                'pontos': 30,
                'categoria': 'Desafio',
                'dica': 'Use divisão inteira para calcular quantas notas de cada valor',
                'explicacao': 'Algoritmo guloso: sempre use a maior nota possível até completar o valor.',
            },
        ]
        
        count = 0
        for ex in exercicios:
            # Verificar se já existe
            if not Exercicio.objects.filter(titulo=ex['titulo']).exists():
                Exercicio.objects.create(**ex)
                count += 1
                self.stdout.write(self.style.SUCCESS(f'Criado: {ex["titulo"]}'))
        
        self.stdout.write(self.style.SUCCESS(f'✅ {count} exercícios criados com sucesso!'))