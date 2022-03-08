from django.urls import path
from .views import Descripcion, jsonArmado, publicar, hola


urlpatterns = [
    path('publicar/', publicar, name="publicar"),
    path('describir/', jsonArmado, name="describir"),
    path('hola/', hola, name="hola"),
]
