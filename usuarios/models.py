# usuarios/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    TIPO_CHOICES = [
        ('ALUNO', 'Aluno'),
        ('PROFESSOR', 'Professor'),
        ('ADMIN', 'Administrador'),
    ]
    
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='ALUNO')
    pontos = models.IntegerField(default=0)
    nivel = models.IntegerField(default=1)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    # Campos opcionais (pode adicionar depois)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    exercicios_resolvidos = models.ManyToManyField(
        'exercicios.Exercicio',
        related_name='resolvido_por',
        blank=True)
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    
    def __str__(self):
        return f"{self.username} ({self.tipo})"