from django import forms
from django.contrib.auth.models import User
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    destinatario = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Para"
    )
    
    class Meta:
        model = Mensaje
        fields = ['destinatario', 'asunto', 'contenido']