from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    jornada_iniciada = models.BooleanField(default=False)
    data_nascimento = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    foto_perfil = models.ImageField(upload_to='perfis/', null=True, blank=True)
    nivel = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)
    trilhas_concluidas = models.IntegerField(default=0)
    exercicios_resolvidos = models.IntegerField(default=0)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    # Links sociais
    linkedin = models.URLField(max_length=200, blank=True)
    github = models.URLField(max_length=200, blank=True)
    website = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
        ordering = ['-data_atualizacao']
    
    def __str__(self):
        return f'Perfil de {self.usuario.username}'
    
    def nome_completo(self):
        if self.usuario.first_name and self.usuario.last_name:
            return f"{self.usuario.first_name} {self.usuario.last_name}"
        return self.usuario.username
    
    def get_nivel_progresso(self):
        """Calcula o progresso para o próximo nível"""
        xp_para_proximo_nivel = self.nivel * 100  # Exemplo: 100 XP por nível
        progresso = min((self.xp % xp_para_proximo_nivel) / xp_para_proximo_nivel * 100, 100)
        return round(progresso, 1)

class LinkSocial(models.Model):
    PLATAFORMAS = [
        ('linkedin', 'LinkedIn'),
        ('github', 'GitHub'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
        ('website', 'Website Pessoal'),
        ('portfolio', 'Portfólio'),
        ('youtube', 'YouTube'),
        ('facebook', 'Facebook'),
        ('outro', 'Outro'),
    ]
    
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='links_sociais')
    plataforma = models.CharField(max_length=20, choices=PLATAFORMAS)
    nome = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    icone = models.CharField(max_length=50, blank=True)
    ordem = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Link Social'
        verbose_name_plural = 'Links Sociais'
        ordering = ['ordem', 'data_criacao']
    
    def __str__(self):
        return f"{self.nome} - {self.perfil.usuario.username}"
    
    def save(self, *args, **kwargs):
        # Define o ícone baseado na plataforma se não estiver definido
        if not self.icone:
            icones = {
                'linkedin': 'fab fa-linkedin',
                'github': 'fab fa-github',
                'instagram': 'fab fa-instagram',
                'twitter': 'fab fa-twitter',
                'website': 'fas fa-globe',
                'portfolio': 'fas fa-briefcase',
                'youtube': 'fab fa-youtube',
                'facebook': 'fab fa-facebook',
                'outro': 'fas fa-link',
            }
            self.icone = icones.get(self.plataforma, 'fas fa-link')
        
        # Define o nome se não estiver definido
        if not self.nome:
            self.nome = dict(self.PLATAFORMAS).get(self.plataforma, self.plataforma.capitalize())
        
        super().save(*args, **kwargs)

class AtividadePerfil(models.Model):
    TIPOS_ATIVIDADE = [
        ('login', 'Login'),
        ('trilha', 'Trilha'),
        ('exercicio', 'Exercício'),
        ('perfil', 'Perfil'),
        ('conquista', 'Conquista'),
        ('sistema', 'Sistema'),
    ]
    
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='atividades')
    tipo = models.CharField(max_length=20, choices=TIPOS_ATIVIDADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    dados = models.JSONField(default=dict, blank=True)  # Para armazenar dados extras
    data = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Atividade de Perfil'
        verbose_name_plural = 'Atividades de Perfil'
        ordering = ['-data']
    
    def __str__(self):
        return f"{self.titulo} - {self.perfil.usuario.username}"

# Signal para criar perfil automaticamente quando um usuário é criado
@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

# Signal para salvar perfil quando usuário é salvo
@receiver(post_save, sender=User)
def salvar_perfil_usuario(sender, instance, **kwargs):
    try:
        instance.perfil.save()
    except Perfil.DoesNotExist:
        Perfil.objects.create(usuario=instance)
    def ganhar_xp(self, quantidade):
        """Adiciona XP ao perfil e verifica level up"""
        self.xp_atual += quantidade
        while self.xp_atual >= self.xp_para_proximo_nivel():
            self.xp_atual -= self.xp_para_proximo_nivel()
            self.nivel += 1
        self.save()
        return self.nivel
    
    def xp_para_proximo_nivel(self):
        """Calcula XP necess�rio para pr�ximo n�vel"""
        return 100 * (self.nivel ** 2) + 100
    
    def progresso_nivel(self):
        """Retorna progresso atual no n�vel (0-100)"""
        xp_necessario = self.xp_para_proximo_nivel()
        return (self.xp_atual / xp_necessario) * 100

