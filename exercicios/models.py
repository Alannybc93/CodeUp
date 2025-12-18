from django.db import models
from trilhas.models import Modulo

class Exercicio(models.Model):
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, related_name='exercicios')
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