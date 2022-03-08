from django.urls import path

from .views import Login
# from .views import 


urlpatterns = [
    path('login/', Login.as_view(), name="login-api"),
]