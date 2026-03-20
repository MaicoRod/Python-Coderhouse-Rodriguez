from django import forms
from .models import Emocion, Categoria, EntradaGratitud

class EmocionForm(forms.ModelForm):
    class Meta:
        model = Emocion
        fields = ['nombre', 'descripcion']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']


class EntradaGratitudForm(forms.ModelForm):
    class Meta:
        model = EntradaGratitud
        fields = ['titulo', 'descripcion', 'imagen', 'emocion', 'categoria']
