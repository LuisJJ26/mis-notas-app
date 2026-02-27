"""
notes/forms.py - Archivo nuevo
"""
from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    """
    Formulario para crear/editar notas
    """
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la nota'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu nota aquí...', 'rows': 5}),
        }
        labels = {
            'title': 'Título',
            'content': 'Contenido',
        }