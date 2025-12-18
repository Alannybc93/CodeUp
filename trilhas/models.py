from django.db import models
from django.conf import settings

class Trilha(models.Model):
    DIFICULDADE_CHOICES = [
        ('iniciante', 'Iniciante'),
        ('intermediario', 'Intermediário'),
        ('avancado', 'Avançado'),
    ]
    
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    icone = models.CharField(max_length=50, default='book')
    cor = models.CharField(max_length=7, default='#FFD700')  # Cor em hex
    dificuldade = models.CharField(max_length=20, choices=DIFICULDADE_CHOICES, default='iniciante')
    tempo_estimado = models.IntegerField(default=0)  # Em horas
    pontos_recompensa = models.IntegerField(default=100)
    ativo = models.BooleanField(default=True)
    ordem = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['ordem', 'data_criacao']
        verbose_name = 'Trilha'
        verbose_name_plural = 'Trilhas'
    
    def __str__(self):
        return self.titulo
    
    def get_modulos_count(self):
        return self.modulos.count()

class Modulo(models.Model):
    trilha = models.ForeignKey(Trilha, on_delete=models.CASCADE, related_name='modulos')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    conteudo = models.TextField(blank=True)  # Conteúdo em Markdown/HTML
    video_url = models.URLField(blank=True)
    ordem = models.IntegerField(default=0)
    duracao = models.IntegerField(default=0)  # Em minutos
    concluido = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['ordem']
        verbose_name = 'Módulo'
        verbose_name_plural = 'Módulos'
    
    def __str__(self):
        return f"{self.trilha.titulo} - {self.titulo}"
    
    def get_exercicios_count(self):
        return self.exercicios.count()

class ProgressoTrilha(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='progresso_trilhas')
    trilha = models.ForeignKey(Trilha, on_delete=models.CASCADE)
    modulo_atual = models.ForeignKey(Modulo, on_delete=models.SET_NULL, null=True, blank=True)
    percentual_concluido = models.FloatField(default=0)
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    concluido = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['usuario', 'trilha']
        verbose_name = 'Progresso de Trilha'
        verbose_name_plural = 'Progressos de Trilhas'
    
    def __str__(self):
        return f"{self.usuario.username} - {self.trilha.titulo}"