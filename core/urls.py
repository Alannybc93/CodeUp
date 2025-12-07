from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trilhas/', views.trails, name='trails'),
    path('trilhas/<int:trail_id>/exercicios/', views.exercises, name='exercises'),
]

urlpatterns = [
    path('', views.home, name='home'),
    path('trails/', views.trails, name='trails'),
]