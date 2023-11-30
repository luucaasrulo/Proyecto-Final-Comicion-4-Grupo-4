from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Categoria
# Create your views here.

class AgregarCatergoria(CreateView):
    model = Categoria
    files = {'nombres'}
    template_name = 'post/agregar_categoria.html'
    success_url = reverse_lazy('inicio')




