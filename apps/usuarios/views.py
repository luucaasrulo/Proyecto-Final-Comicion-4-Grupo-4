from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Usuarios
from .forms import RegistrarUsuariosForm
# Create your views here.

class RegristrarUsuario(CreateView):
    model = Usuarios
    from_class = RegistrarUsuariosForm
    template_name = 'usuario/registrar_usuario.html'
    success_url = reverse_lazy('inicio')