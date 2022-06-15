from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.conf import settings
import os


class Post(models.Model):
    titulo_post = models.CharField(max_length=255, verbose_name='Título')
    # Verbose_name serve para mudar o título das colunas na página de admin
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')  # Para quando deletar um usuário, não fazer nada
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    conteudo_post = models.TextField(verbose_name='Conteúdo')  # Para textos grandes
    excerto_post = models.TextField(verbose_name='Excerto')
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria')
    # Permite deletar e não fazer nada, pode deixar em branco e null permite deixar um post sem categoria.
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    # Indica o local onde vai armazenar as imagens
    publicado_post = models.BooleanField(default=False, verbose_name='Publicado')
    # faz com que o post não seja publicado diretamente, sendo necessário confirmar primeiro para depois publicar

    def __str__(self):
        return self.titulo_post

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagem_post:
            self.resize_image(self.imagem_post.name, 800)   # Redimensionando as imagens

    @staticmethod
    def resize_image(img_name, new_width):
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)  # Caminho do arquivo imagem
        img = Image.open(img_path)
        width, height = img.size
        new_height = round((new_width * height) / width)    # Pegando a nova altura para redimensionar

        if width <= new_width:
            img.close()
            return

        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(
            img_path,
            optimize=True,
            quality=60
        )
        new_img.close()



# Create your models here.
