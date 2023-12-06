from django.urls import path
from .views import agregar_comentario, ModificarComentario, EliminarComentario

app_name = 'apps.comentarios'

urlpatterns = [
    path('agregar_comentario/', agregar_comentario, name='agregar_comentario'),
    path('modificar_comentario/<int:pk>', ModificarComentario.as_view(), name='modificar_comentario'),
    path('confirma_eliminar/<int:pk>', EliminarComentario.as_view(), name='confirma_eliminar'),
]
