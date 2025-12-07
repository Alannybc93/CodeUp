# exercicios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='exercicios_index'),
    path('<int:exercicio_id>/', views.detalhe, name='exercicios_detalhe'),
    path('<int:exercicio_id>/resolver/', views.resolver, name='exercicios_resolver'),
    path('meus/', views.meus_exercicios, name='meus_exercicios'),
]