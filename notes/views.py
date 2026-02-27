"""
notes/views.py - REEMPLAZA TODO EL CONTENIDO
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Note
from .forms import NoteForm

# Vistas basadas en funciones (para login/logout usaremos las de Django)
@login_required
def note_list(request):
    """Vista para listar las notas del usuario"""
    notes = Note.objects.filter(owner=request.user)
    return render(request, 'notes/note_list.html', {'notes': notes})

@login_required
def note_detail(request, pk):
    """Vista para ver una nota específica"""
    note = get_object_or_404(Note, pk=pk, owner=request.user)
    return render(request, 'notes/note_detail.html', {'note': note})

@login_required
def note_create(request):
    """Vista para crear una nueva nota"""
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form, 'action': 'Crear'})

@login_required
def note_update(request, pk):
    """Vista para editar una nota"""
    note = get_object_or_404(Note, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form, 'action': 'Editar'})

@login_required
def note_delete(request, pk):
    """Vista para eliminar una nota"""
    note = get_object_or_404(Note, pk=pk, owner=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})