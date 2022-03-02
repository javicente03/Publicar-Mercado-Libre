from django.urls import path
from .views import Descripcion, jsonArmado, publicar


urlpatterns = [
    path('publicar/', publicar, name="publicar"),
    path('describir/', jsonArmado, name="describir")
]
