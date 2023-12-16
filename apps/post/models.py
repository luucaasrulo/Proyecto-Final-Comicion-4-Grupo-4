from django.db import models
from apps.usuarios.models import Usuarios
from ckeditor.fields import RichTextField

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=40, null=False, unique=True)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=30, null=False )
    autor = models.CharField(max_length=20, null=True, default="desconocido")
    resumen = models.CharField(max_length=90, null=False)
    contenido = RichTextField()
    activo = models.BooleanField(default=True)
    fecha_post = models.DateTimeField(auto_now_add=True)
    colaborador = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True, default="desconocido")
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(null=True,blank=True,upload_to='post',default='post/default2.png', help_text="imagen 16:9 ó 370x140px")
    contador_visitas = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo
    
    def aumentar_contador(self):
        self.contador_visitas += 1
        self.save()
        
    class Meta:
         ordering = ('-fecha_post',)