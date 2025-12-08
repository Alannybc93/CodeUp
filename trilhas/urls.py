# trilhas/urls.py - COMPLETO E CORRETO
from django.urls import path
from . import views

app_name = 'trilhas'  # ← ESSENCIAL! ADICIONE ESTA LINHA

urlpatterns = [
    # Página principal das trilhas
    path('', views.trilhas, name='trilhas'),  # ← Note: name='trilhas' (não 'index')
    
    # Trilhas específicas
    path('python/', views.trilha_detalhe, {'nome_trilha': 'python'}, name='trilha_python'),
    path('javascript/', views.trilha_detalhe, {'nome_trilha': 'javascript'}, name='trilha_javascript'),
    path('sql/', views.trilha_detalhe, {'nome_trilha': 'sql'}, name='trilha_sql'),
    path('web/', views.trilha_detalhe, {'nome_trilha': 'web'}, name='trilha_web'),
    path('algoritmos/', views.trilha_detalhe, {'nome_trilha': 'algoritmos'}, name='trilha_algoritmos'),
    path('datascience/', views.trilha_detalhe, {'nome_trilha': 'datascience'}, name='trilha_datascience'),
]