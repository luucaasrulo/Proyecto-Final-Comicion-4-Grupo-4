from django.urls import path,include
from django.contrib.auth.views import LoginView, LogoutView
 
from .views import RegristrarUsuario, ActualizarUsuario, EliminarUsuario, listar_usuarios,Perfil


app_name = 'apps.usuarios'

urlpatterns = [
    path('registrar/', RegristrarUsuario.as_view(), name='registrar'),
    path('iniciar_sesion/', LoginView.as_view(template_name = 'usuarios/iniciar_sesion.html'), name='iniciar_sesion'),
    path('login/', LoginView.as_view(template_name = 'usuarios/iniciar_sesion_modal.html'), name='login'),
    path('cerrar_sesion/', LogoutView.as_view(), name='cerrar_sesion'),
    path("actualizar_usuario/<int:pk>", ActualizarUsuario.as_view(template_name = 'usuarios/actualizar_usuario.html'), name='actualizar_usuario'),
    path("eliminar_usuario/<int:pk>", EliminarUsuario.as_view(), name='eliminar_usuario'),
    path("listar_usuarios/", listar_usuarios, name='listar_usuarios'),
    path("perfil/<int:pk>", Perfil.as_view(template_name = 'usuarios/perfil.html'), name ='perfil'),
]




