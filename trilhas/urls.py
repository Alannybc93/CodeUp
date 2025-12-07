from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='trilhas_index'),
    path('<int:trilha_id>/', views.detalhe, name='trilhas_detalhe'),
    path('<int:trilha_id>/iniciar/', views.iniciar_trilha, name='trilhas_iniciar'),
    path('<int:trilha_id>/modulo/<int:modulo_id>/', views.modulo_detalhe, name='trilhas_modulo'),
]