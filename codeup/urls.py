# codeup/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import home
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='inicio'),
    path('usuarios/', include('usuarios.urls')),
    
    # Apps básicos apenas
    path('trilhas/', include('trilhas.urls')),
    path('exercicios/', include('exercicios.urls')),
    
    # Favicon
    path('favicon.ico', RedirectView.as_view(
        url='/static/img/favicon.ico',
        permanent=True
    )),
]

# Servir arquivos estáticos
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)