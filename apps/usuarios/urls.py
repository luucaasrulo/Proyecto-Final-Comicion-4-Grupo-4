from django.urls import path
from .views import *


app_name = 'apps.usuarios'

urlpatterns = [
    path('registrar/', RegristrarUsuario.as_view(), name='registrar'),
]
