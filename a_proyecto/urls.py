from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index, name='inicio'),
    path('contacto/',contacto, name='contacto'),
    path('usuarios/', include('apps.usuarios.urls')),
]
