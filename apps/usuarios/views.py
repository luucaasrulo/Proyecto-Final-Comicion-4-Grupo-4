from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Usuarios
from .forms import RegistrarUsuariosForm


# Create your views here.
class RegristrarUsuario(CreateView):
    model = Usuarios
    form_class = RegistrarUsuariosForm
    template_name = 'usuarios/registrar_usuario.html'
    success_url = reverse_lazy('inicio')

class ActualizarUsuario(LoginRequiredMixin,UpdateView):
    model = Usuarios
    fields= ['nombre','apellido','email','fecha_nacimiento', 'imagen']
    template_name = 'usuarios/actualizar_usuario.html'
    success_url = reverse_lazy('inicio')

class EliminarUsuario(LoginRequiredMixin,DeleteView):
    model = Usuarios
    template_name = 'post/confirmar_eliminar.html'
    success_url = reverse_lazy('apps.usuarios:listar_usuarios')

def listar_usuarios(request):
    usuarios = Usuarios.objects.all().exclude(is_superuser = 1)
    template_name = 'usuarios/listar_usuarios.html'
    contexto = {
        "usuarios" : usuarios
    }
    return render(request, template_name, contexto)

class Perfil(CreateView):
    model = Usuarios
    fields= ['nombre','apellido','email','fecha_nacimiento', 'imagen']
    template_name = 'usuarios/perfil.html'
    success_url = reverse_lazy('inicio')
