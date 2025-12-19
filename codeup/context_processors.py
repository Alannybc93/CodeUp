# codeup/context_processors.py
def site_info(request):
    """Adiciona informações do site ao contexto de templates"""
    from django.conf import settings
    
    return {
        'SITE_NAME': getattr(settings, 'SITE_NAME', 'CodeUP'),
        'SITE_DESCRIPTION': getattr(settings, 'SITE_DESCRIPTION', 'Plataforma de aprendizado'),
        'SITE_VERSION': getattr(settings, 'SITE_VERSION', '1.0.0'),
        'SITE_URL': getattr(settings, 'SITE_URL', 'http://localhost:8000'),
        'DEBUG': settings.DEBUG,
    }