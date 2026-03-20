from django.urls import path
from . import views

urlpatterns = [
    path('', views.mensajes, name='mensajes'),
    path('enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('<int:pk>/', views.ver_mensaje, name='ver_mensaje'),
    path('<int:pk>/eliminar/', views.eliminar_mensaje, name='eliminar_mensaje'),
]