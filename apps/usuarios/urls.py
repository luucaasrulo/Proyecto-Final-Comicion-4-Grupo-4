from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
 
from .views import *


app_name = 'apps.usuarios'

urlpatterns = [
    path('registrar/', RegristrarUsuario.as_view(), name='registrar'),
    path('iniciar_sesion/', LoginView.as_view(template_name = 'usuarios/iniciar_sesion.html'), name='iniciar_sesion'),
    path('cerrar_sesion/', LogoutView.as_view(), name='cerrar_sesion'),
]




