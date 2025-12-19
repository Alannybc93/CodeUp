"""
usuarios/urls.py - URLs do app de usuários
VERSÃO COMPLETA E CORRIGIDA
"""
from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    # ========== PÁGINA INICIAL ==========
    path('', views.home, name='home'),
    
    # ========== AUTENTICAÇÃO ==========
    path('login/', views.login_view, name='login'),
    path('registrar/', views.registrar, name='registrar'),
    path('logout/', views.logout_view, name='logout'),
    
    # ========== PERFIL ==========
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/alterar-senha/', views.alterar_senha, name='alterar_senha'),
    path('perfil/configurar/', views.configurar_conta, name='configurar_conta'),
    path('perfil/excluir/', views.excluir_conta, name='excluir_conta'),
    path('perfil/publico/', views.perfil_publico, name='perfil_publico'),
    path('perfil/publico/<str:username>/', views.perfil_publico, name='perfil_publico_usuario'),
    
    # ========== DASHBOARD E JORNADA ==========
    path('dashboard/', views.dashboard, name='dashboard'),
    path('iniciar-jornada/', views.iniciar_jornada, name='iniciar_jornada'),
    path('tutorial/', views.tutorial_inicial, name='tutorial_inicial'),
    path('concluir-tutorial/', views.concluir_tutorial, name='concluir_tutorial'),
    
    # ========== ADMIN ==========
    path('admin/painel/', views.painel_admin, name='painel_admin'),
    path('admin/usuarios/', views.gerenciar_usuarios, name='gerenciar_usuarios'),
    path('admin/usuario/<int:usuario_id>/', views.detalhes_usuario, name='detalhes_usuario'),
    path('admin/usuario/<int:usuario_id>/editar/', views.editar_usuario_admin, name='editar_usuario_admin'),
    path('admin/usuario/<int:usuario_id>/resetar-senha/', views.resetar_senha_admin, name='resetar_senha_admin'),
    path('admin/usuario/<int:usuario_id>/excluir/', views.excluir_usuario_admin, name='excluir_usuario_admin'),
    path('admin/usuario/<int:usuario_id>/promover/', views.promover_usuario, name='promover_usuario'),
    path('admin/usuario/<int:usuario_id>/adicionar-xp/', views.adicionar_xp, name='adicionar_xp'),
    
    # ========== SISTEMA ==========
    path('admin/sistema/status/', views.sistema_status, name='sistema_status'),
    path('admin/sistema/manutencao/', views.executar_manutencao, name='executar_manutencao'),
    
    # ========== SUPORTE ==========
    path('teste/', views.teste, name='teste'),
    path('acesso-negado/', views.acesso_negado, name='acesso_negado'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    
    # ========== API ==========
    path('api/perfil/', views.api_perfil, name='api_perfil'),
    path('api/estatisticas/', views.api_estatisticas, name='api_estatisticas'),
    
    # ========== LANDING PAGE ==========
    path('landing/', views.landing_page, name='landing_page'),
]