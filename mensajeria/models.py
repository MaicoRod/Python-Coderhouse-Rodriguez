from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    asunto = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(default=timezone.now)
    leido = models.BooleanField(default=False)
    
    def __str__(self):
        return f"De {self.remitente} para {self.destinatario}: {self.asunto}"
    
    class Meta:
        verbose_name_plural = "Mensajes"
        ordering = ['-fecha_envio']