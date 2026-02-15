from django.db import models
from django.utils import timezone

class Emocion(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural="Emociones"

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural="Categorias"

class EntradaGratitud(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    emocion = models.ForeignKey(Emocion, on_delete=models.SET_NULL, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural="Entradas de Gratitud"
        ordering=['-fecha_creacion']
