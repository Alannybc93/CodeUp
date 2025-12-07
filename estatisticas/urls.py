# estatisticas/urls.py
from django.urls import path
from estatisticas import views

urlpatterns = [
    path('dashboard/', views.dashboard_estatisticas, name='dashboard_estatisticas'),
]