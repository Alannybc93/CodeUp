from django.db import models

class Medalha(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    icone = models.CharField(max_length=100)
    pontos_necessarios = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nome