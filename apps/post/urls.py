from django.urls import path

from .views import AgregarCatergoria, AgregarPost,ListarPost,EliminarPost,ModificarPost,contenido_post, listar_por_categoria, ordenar_por, listar_primeros_post


app_name = 'apps.post'

urlpatterns = [
    path('agregar_categoria/', AgregarCatergoria.as_view(), name='agregar_categoria'),
    path('agregar_post/', AgregarPost.as_view(), name= 'agregar_post' ),
    path('listar_post/', ListarPost.as_view(), name='listar_post'),
    path('modificar_post/<int:pk>', ModificarPost.as_view(), name='modificar_post'),
    path('confirmar_eliminar/<int:pk>', EliminarPost.as_view(), name='confirmar_eliminar'),
    path('contenido_post/<int:id>', contenido_post, name='contenido_post'),
    path('listar_por_categoria/<str:categoria>', listar_por_categoria, name='listar_por_categoria'),
    path('ordenar_por/', ordenar_por, name='ordenar_por'),
    path('listar_primeros_post/', listar_primeros_post, name='listar_primeros_post'),  
]


