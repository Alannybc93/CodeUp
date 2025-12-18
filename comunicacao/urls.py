from django.urls import path
from comunicacao import views

app_name = "comunicacao"

urlpatterns = [
    path("", views.lista_foruns, name="lista_foruns"),
]
