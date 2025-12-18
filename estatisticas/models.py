from django.db import models
from django.conf import settings  # Importe settings
# REMOVA: from django.contrib.auth.models import User

class EstatisticaUsuario(models.Model):
    # CORRIJA ESTA LINHA:
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # ← Use settings.AUTH_USER_MODEL
        on_delete=models.CASCADE
    )
    total_pontos = models.IntegerField(default=0)
    exercicios_resolvidos = models.IntegerField(default=0)
    tempo_total_estudo = models.IntegerField(default=0)  # em minutos
    ultimo_acesso = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Estatísticas de {self.usuario.username}"