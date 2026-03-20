from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Emocion(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Emociones"


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Categorías"


class EntradaGratitud(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=250, blank=True)
    descripcion = RichTextField()
    imagen = models.ImageField(upload_to='entradas/', blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    emocion = models.ForeignKey(Emocion, on_delete=models.SET_NULL, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = "Entradas de Gratitud"
        ordering = ['-fecha_creacion']