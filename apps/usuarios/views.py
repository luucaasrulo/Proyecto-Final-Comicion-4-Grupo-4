from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Usuarios
from .forms import RegistrarUsuariosForm
# Create your views here.

class RegristrarUsuario(CreateView):
    model = Usuarios
    form_class = RegistrarUsuariosForm
    template_name = 'usuarios/registrar_usuario.html'
    success_url = reverse_lazy('inicio')