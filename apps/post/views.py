
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy


from .models import Categoria, Post
# Create your views here.

class AgregarCatergoria(CreateView):
    model = Categoria
    fields = {'nombre'}
    template_name = 'post/agregar_categoria.html'
    success_url = reverse_lazy('inicio')

class AgregarPost(CreateView):
    model = Post
    fields = ['titulo','resumen','contenido','categoria','imagen']
    template_name = 'post/agregar_post.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.colaborador = self.request.user
        return super().form_valid(form)

class ModificarPost(UpdateView):
    model = Post
    fields = ['titulo','resumen','contenido','categoria','imagen']
    template_name = 'post/modificar_post.html'
    success_url = reverse_lazy('inicio')  

class ListarPost(ListView):
    model= Post
    template_name = 'post/listar_post.html'
    context_object_name = 'post'

class EliminarPost(DeleteView):
    model = Post
    template_name = 'post/confirmar_eliminar.html'

class ContenidoPost(DetailView):
    model = Post
    template_name = 'post/contenido_post.html'
    context_object_name = 'post'
    



