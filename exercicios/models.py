# exercicios/models.py
from django.db import models
from django.contrib.auth.models import User

class Exercicio(models.Model):
    # Nota: Modulo está em trilhas.models, não em exercicios.models
    modulo = models.ForeignKey('trilhas.Modulo', on_delete=models.CASCADE, related_name='exercicios')
    titulo = models.CharField(max_length=200)
    enunciado = models.TextField()
    codigo_inicial = models.TextField(blank=True)
    resposta_correta = models.TextField()
    pontos = models.IntegerField(default=10)
    dificuldade = models.CharField(max_length=20, choices=[
        ('facil', 'Fácil'),
        ('medio', 'Médio'),
        ('dificil', 'Difícil'),
    ])
    
    def __str__(self):
        return f"{self.titulo} - {self.modulo.titulo}"

class RespostaAluno(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('correto', 'Correto'),
        ('incorreto', 'Incorreto'),
        ('parcial', 'Parcialmente Correto'),
    ]
    
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='respostas_exercicios')
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE, related_name='respostas')
    resposta = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    tentativas = models.IntegerField(default=1)
    pontos_ganhos = models.IntegerField(default=0)
    tempo_gasto = models.IntegerField(default=0, help_text="Tempo gasto em segundos")
    data_submissao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.aluno.username} - {self.exercicio.titulo}"
    
    class Meta:
        verbose_name = 'Resposta do Aluno'
        verbose_name_plural = 'Respostas dos Alunos'
        ordering = ['-data_submissao']