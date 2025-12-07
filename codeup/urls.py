# codeup/urls.py - VERSÃO LIMPA E FUNCIONAL
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from usuarios import views as usuarios_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Página inicial
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    
    # Autenticação (Django built-in)
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    
    # Cadastro (nossa view personalizada)
    path('cadastro/', usuarios_views.registrar, name='cadastro'),
    
    # Apps principais (JÁ FUNCIONAM)
    path('trilhas/', include('trilhas.urls')),
    path('exercicios/', include('exercicios.urls')),
    
    # NÃO TEMOS DASHBOARD POR ENQUANTO - REMOVIDO
]

# Adicione esta linha se quiser redirect de /dashboard para home
# from django.views.generic import RedirectView
# urlpatterns.append(path('dashboard/', RedirectView.as_view(url='/'), name='dashboard'))