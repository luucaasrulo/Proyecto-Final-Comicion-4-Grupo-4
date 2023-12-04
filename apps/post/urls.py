from django.urls import path



from .views import AgregarCatergoria, AgregarPost,ListarPost,EliminarPost,ModificarPost,ContenidoPost


app_name = 'apps.post'

urlpatterns = [
    path('agregar_categoria/', AgregarCatergoria.as_view(), name='agregar_categoria'),
    path('agregar_post/', AgregarPost.as_view(), name= 'agregar_post' ),
    path('listar_post/', ListarPost.as_view(), name='listar_post'),
    path('modificar_post/<int:pk>', ModificarPost.as_view(), name='modificar_post'),
    path('confirmar_eliminar/<int:pk>', EliminarPost.as_view(), name='confirmar_eliminar'),
    path('contenido_post/<int:pk>', ContenidoPost.as_view(), name='contenido_post'),
]


