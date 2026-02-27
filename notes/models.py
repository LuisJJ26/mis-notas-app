"""
notes/models.py - REEMPLAZA TODO EL CONTENIDO
"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Note(models.Model):
    """
    Modelo para las notas de los usuarios
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    
    class Meta:
        ordering = ['-created_at']  # Las más recientes primero
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
    
    def __str__(self):
        return f"{self.title} - {self.owner.username}"
    
    def get_absolute_url(self):
        return reverse('note_detail', args=[str(self.id)])