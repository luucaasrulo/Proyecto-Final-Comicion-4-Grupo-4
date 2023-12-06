from typing import Any
from django.db import models
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView

from .forms import ComentarioForm
from .models import Comentario

# Create your views here.

def agregar_comentario(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    contexto = {
        'form': form,
    }

    template_name = 'comentarios/agregar_comentario.html'
    return render(request, template_name, contexto)

class ModificarComentario(LoginRequiredMixin, UpdateView):
    model = Comentario
    fields = ['texto']
    template_name = 'comentarios/modificar_comentario.html'

    def get_success_url(self):
        detalle_url = reverse('apps.post:contenido_post', kwargs={'id': self.object.post.id})
        return detalle_url
    
    def get_context_data(self):
        context = super().get_context_data()
        post = self.object.post
        comentarios = Comentario.objects.filter(post=post.id)
        context['post'] = post
        context['comentarios'] = comentarios
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(usuario=self.request.user)
    
class EliminarComentario(LoginRequiredMixin,DeleteView):
    model = Comentario
    template_name = 'comentarios/confirma_eliminar.html'
    context_object_name = 'comentario'

    def get_success_url(self):
        detalle_url = reverse('apps.post:contenido_post', kwargs={'id': self.object.post.id})
        return detalle_url

