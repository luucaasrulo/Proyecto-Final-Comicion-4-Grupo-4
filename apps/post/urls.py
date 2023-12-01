from django.urls import path



from .views import AgregarCatergoria, AgregarPost,ListarPost


app_name = 'apps.post'

urlpatterns = [
    path('agregar_categoria/', AgregarCatergoria.as_view(), name='agregar_categoria'),
    path('agregar_post/', AgregarPost.as_view, name= 'agregar_post' ),
    path('listar_post', ListarPost.as_view(), name='listar_post'),
]


