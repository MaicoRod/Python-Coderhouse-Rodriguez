from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares/', blank=True, null=True)
    biografia = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"Perfil de {self.user.username}"
    
    class Meta:
        verbose_name_plural = "Perfiles"