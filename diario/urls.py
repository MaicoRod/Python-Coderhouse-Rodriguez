from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    
    # Pages (Entradas)
    path('pages/', views.EntradaListView.as_view(), name='entrada_list'),
    path('pages/<int:pk>/', views.EntradaDetailView.as_view(), name='entrada_detail'),
    path('pages/crear/', views.EntradaCreateView.as_view(), name='entrada_create'),
    path('pages/<int:pk>/editar/', views.EntradaUpdateView.as_view(), name='entrada_update'),
    path('pages/<int:pk>/borrar/', views.EntradaDeleteView.as_view(), name='entrada_delete'),
    
    # Gestión
    path('emociones/', views.emociones, name='emociones'),
    path('categorias/', views.categorias, name='categorias'),
]