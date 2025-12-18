# trilhas/urls.py - VERSÃO COM 'lista'
from django.urls import path
from . import views

app_name = 'trilhas'

urlpatterns = [
    # Mude para 'lista' se quiser usar trilhas:lista
    path('', views.trilhas, name='lista'),  # ← ALTERE PARA 'lista'
    
    path('python/', views.trilha_detalhe, {'nome_trilha': 'python'}, name='trilha_python'),
    path('javascript/', views.trilha_detalhe, {'nome_trilha': 'javascript'}, name='trilha_javascript'),
    path('sql/', views.trilha_detalhe, {'nome_trilha': 'sql'}, name='trilha_sql'),
    path('web/', views.trilha_detalhe, {'nome_trilha': 'web'}, name='trilha_web'),
    path('algoritmos/', views.trilha_detalhe, {'nome_trilha': 'algoritmos'}, name='trilha_algoritmos'),
    path('datascience/', views.trilha_detalhe, {'nome_trilha': 'datascience'}, name='trilha_datascience'),
]