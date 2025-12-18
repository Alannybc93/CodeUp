# usuarios/decorators.py
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test

def nivel_requerido(nivel_minimo):
    """Decorator para verificar nível do usuário"""
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.nivel >= nivel_minimo:
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied("Você não tem permissão para acessar esta página.")
        return _wrapped_view
    return decorator

def administrador_required(view_func):
    """Decorator para administradores"""
    return user_passes_test(
        lambda u: u.is_authenticated and (u.nivel >= 50 or u.is_superuser),
        login_url='/acesso-negado/'
    )(view_func)

def moderador_required(view_func):
    """Decorator para moderadores"""
    return user_passes_test(
        lambda u: u.is_authenticated and (u.nivel >= 10 or u.is_staff),
        login_url='/acesso-negado/'
    )(view_func)