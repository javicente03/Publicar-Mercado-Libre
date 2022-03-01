from django.urls import path
from .views import publicar


urlpatterns = [
    path('publicar/', publicar, name="publicar")
]
