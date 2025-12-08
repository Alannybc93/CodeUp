# codeup/debug_views.py
from django.http import HttpResponse
import inspect

def find_redirect(request):
    """Descobre quem está redirecionando"""
    
    html = "<h1>🔍 DEBUG - FIND REDIRECT</h1>"
    
    # 1. Verifica todas as views importadas
    import trilhas.views
    html += "<h2>trilhas.views:</h2>"
    for name, obj in inspect.getmembers(trilhas.views):
        if inspect.isfunction(obj):
            html += f"<p>{name}</p>"
    
    # 2. Testa a view trilhas diretamente
    from trilhas.views import trilhas
    import django.test
    client = django.test.Client()
    response = client.get('/trilhas/')
    
    html += f"<h2>Response from /trilhas/:</h2>"
    html += f"<p>Status: {response.status_code}</p>"
    if hasattr(response, 'url'):
        html += f"<p>Redirects to: {response.url}</p>"
    
    return HttpResponse(html)