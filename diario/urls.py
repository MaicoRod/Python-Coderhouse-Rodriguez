from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('entradas/', views.entradas, name='entradas'),
    path('emociones/', views.emociones, name='emociones'),
    path('categorias/', views.categorias, name='categorias'),
]

