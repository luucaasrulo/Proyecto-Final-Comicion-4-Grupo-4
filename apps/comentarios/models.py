from django.db import models
from apps.usuarios.models import Usuarios
from apps.post.models import Post

# Create your models here.
class Comentario(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto
    
    class Meta:
        ordering = ['-fecha']