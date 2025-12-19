from django.contrib import admin
from .models import Perfil, LinkSocial, AtividadePerfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'nivel', 'xp', 'trilhas_concluidas', 'exercicios_resolvidos', 'data_cadastro']
    list_filter = ['nivel', 'jornada_iniciada']
    search_fields = ['usuario__username', 'usuario__email', 'bio']
    readonly_fields = ['data_cadastro', 'data_atualizacao']

@admin.register(LinkSocial)
class LinkSocialAdmin(admin.ModelAdmin):
    list_display = ['nome', 'perfil', 'plataforma', 'url', 'ativo', 'ordem']
    list_filter = ['plataforma', 'ativo']
    search_fields = ['nome', 'url', 'perfil__usuario__username']

@admin.register(AtividadePerfil)
class AtividadePerfilAdmin(admin.ModelAdmin):
    list_display = ['perfil', 'tipo', 'titulo', 'data']
    list_filter = ['tipo', 'data']
    search_fields = ['titulo', 'descricao', 'perfil__usuario__username']
    readonly_fields = ['data']