from django.contrib import admin
from .models import Emocion, Categoria, EntradaGratitud

@admin.register(Emocion)
class EmocionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(EntradaGratitud)
class EntradaGratitudAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'emocion', 'categoria', 'fecha_creacion')
    list_filter = ('emocion', 'categoria', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion')