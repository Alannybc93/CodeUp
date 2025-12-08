# codeup/urls.py - VERSÃO FINAL
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from usuarios import views as usuarios_views
from django.contrib.auth import views as auth_views

# View da página inicial
def home_view(request):
    """
    View da página inicial.
    Sempre mostra home.html, nunca redireciona.
    """
    # Debug opcional
    if request.GET.get('debug'):
        print(f"🏠 Home acessada | User: {request.user}")
    
    return TemplateView.as_view(template_name='home.html')(request)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Página inicial
    path('', home_view, name='home'),
    
    # Autenticação
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=False,  # Não redireciona automaticamente
    ), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'  # Vai para home após logout
    ), name='logout'),
    
    # Cadastro
    path('cadastro/', usuarios_views.registrar, name='cadastro'),
    
    # Apps principais
    path('trilhas/', include('trilhas.urls')),
    path('exercicios/', include('exercicios.urls')),
]

# Middleware de segurança (opcional)
from django.utils.deprecation import MiddlewareMixin

class HomeProtectionMiddleware(MiddlewareMixin):
    """Garante que a home nunca redirecione"""
    def process_response(self, request, response):
        # Se for um redirecionamento da raiz, bloqueia
        if (request.path == '/' and 
            response.status_code in [301, 302, 303, 307, 308] and
            hasattr(response, 'url') and 
            response.url != '/'):
            
            # Retorna a home em vez do redirecionamento
            return TemplateView.as_view(template_name='home.html')(request)
        
        return response