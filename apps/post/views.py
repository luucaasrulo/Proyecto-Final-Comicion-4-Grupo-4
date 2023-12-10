from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy, reverse

from .models import Categoria, Post
from apps.comentarios.models import Comentario
from apps.comentarios.forms import ComentarioForm

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
    fields = ['titulo','resumen','contenido','categoria', 'imagen']
    template_name = 'post/modificar_post.html'
    success_url = reverse_lazy('inicio')  

class ListarPost(ListView):
    model= Post
    template_name = 'post/listar_post.html'
    context_object_name = 'post'
    paginate_by = 3

    def get_context_data(self):
        context = super().get_context_data()
        categorias = Categoria.objects.all()
        context['categorias'] = categorias
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains = query)
        return queryset.order_by('-fecha_post')

class EliminarPost(DeleteView):
    model = Post
    template_name = 'post/confirmar_eliminar.html'
    success_url = reverse_lazy('inicio')

def contenido_post(request,id):
    post = Post.objects.get(id=id)
    comentarios = Comentario.objects.filter(post=id)
    form = ComentarioForm(request.POST)

    if form.is_valid():
        if request.user.is_authenticated:
            aux = form.save(commit=False)
            aux.post = post
            aux.usuario = request.user
            aux.save()
            detalle_url = reverse('apps.post:contenido_post', kwargs={'id': post.id})
            return HttpResponseRedirect(detalle_url)
        else:
            return redirect('apps.usuarios:iniciar_sesion')
    
    contexto = {
        'post': post,
        'form': form,
        'comentarios': comentarios
    }
    template_name = 'post/contenido_post.html'
    return render(request,template_name,contexto)
    
def listar_por_categoria(request, categoria):
    categoria = Categoria.objects.filter(nombre = categoria)
    post = Post.objects.filter(categoria = categoria[0].id).order_by('fecha_post')
    categorias = Categoria.objects.all()
    template_name = 'post/listar_post.html'
    contexto = {
        'post': post,
        'categorias' : categorias,        
    }
    return render(request,template_name,contexto)

def ordenar_por(request):
    orden = request.GET.get('orden', '')
    if orden == 'fecha':
        post = Post.objects.order_by('-fecha_post')
    elif orden == 'titulo':
        post = Post.objects.order_by('titulo')
    else:
        post = Post.objects.all()
    template_name = 'post/listar_post.html'
    contexto = {
        'post' : post
    }
    return render(request, template_name, contexto)

def listar_primeros_post(request):
        post = Post.objects.all()[:2]
        template_name = 'index.html'
        contexto = {
            "post" : post
        }
        return render(request, template_name, contexto)  