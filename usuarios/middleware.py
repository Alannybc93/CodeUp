# usuarios/middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class JornadaInicialMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        
        # Verifica se usuário está autenticado e não completou tutorial
        if request.user.is_authenticated:
            if not request.user.tutorial_concluido:
                # URLs que o usuário pode acessar sem tutorial
                urls_permitidas = [
                    reverse('usuarios:iniciar_jornada'),
                    reverse('usuarios:tutorial_inicial'),
                    reverse('usuarios:concluir_tutorial'),
                    reverse('usuarios:logout'),
                    reverse('usuarios:perfil'),
                    reverse('usuarios:editar_perfil'),
                ]
                
                # Se não estiver em uma URL permitida, redireciona
                if request.path not in urls_permitidas:
                    return redirect('usuarios:iniciar_jornada')
        
        return response