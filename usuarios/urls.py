# usuarios/urls.py
from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
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
    
    # ========== PERFIL PÚBLICO ==========
    path('perfil/publico/', views.perfil_publico, name='perfil_publico'),  # Perfil do próprio usuário
    path('perfil/publico/<str:username>/', views.perfil_publico, name='perfil_publico_usuario'),  # Perfil de outro usuário
    
    # ========== JORNADA INICIAL ==========
    path('iniciar-jornada/', views.iniciar_jornada, name='iniciar_jornada'),
    path('tutorial/', views.tutorial_inicial, name='tutorial_inicial'),
    path('concluir-tutorial/', views.concluir_tutorial, name='concluir_tutorial'),
    
    # ========== DASHBOARD ==========
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # ========== PAINEL ADMINISTRATIVO ==========
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
    
    # ========== ACESSO NEGADO ==========
    path('acesso-negado/', views.acesso_negado, name='acesso_negado'),
]