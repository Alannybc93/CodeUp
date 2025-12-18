from django.urls import path
from . import views

app_name = 'exercicios'

urlpatterns = [
    path('', views.index, name='exercicios_index'),
    path('', views.index, name='index'),  # Alias mais simples
    path('', views.index, name='lista'),  # Alias para compatibilidade
    path('meus/', views.meus_exercicios, name='meus_exercicios'),
    path('<int:exercicio_id>/', views.detalhe, name='exercicios_detalhe'),
    path('<int:exercicio_id>/resolver/', views.resolver, name='exercicios_resolver'),
]