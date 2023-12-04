from django.db import models
from apps.usuarios.models import Usuarios

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=20, null=False)
    autor = models.CharField(max_length=20, null=False)
    resumen = models.TextField()
    contenido = models.TextField()
    fecha_post = models.DateTimeField(auto_now_add=True)
    colaborador = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True,default=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(null=True,blank=True,upload_to='post',default='post/default2.png')

    def __str__(self):
        return self.titulo
    
    class Meta:
         ordering = ('-fecha_post',)