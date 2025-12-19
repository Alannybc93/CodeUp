# exercicios/urls.py
from django.urls import path
from . import views

app_name = 'exercicios'

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),
    path('lista/', views.index, name='lista'),
    
    # Página do usuário
    path('meus/', views.meus_exercicios, name='meus_exercicios'),
    
    # Detalhes do exercício
    path('<int:exercicio_id>/', views.detalhe, name='detalhe'),
    
    # Resolver exercício
    path('<int:exercicio_id>/resolver/', views.resolver_exercicio, name='resolver'),
    
    # Ver resultado
    path('resposta/<int:resposta_id>/resultado/', views.ver_resultado, name='resultado'),
]
