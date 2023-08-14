# weather_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Define las URL aquí
    path('', views.home, name='home'),  # Ruta de la página de inicio
]
