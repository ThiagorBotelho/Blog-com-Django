from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from posts.models import Post
from django.db.models import Q, Count, Case, When
from comentarios.forms import FormComentario
from comentarios.models import Comentario
from django.contrib import messages


class PostIndex(ListView):     # Listview é uma class pronta do django
    model = Post
    template_name = 'posts/index.html'  # Carrega o arquivo css e html
    paginate_by = 6
    context_object_name = 'posts'

    def get_queryset(self):  # altera o modo de visualização dos posts
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(publicado_post=True)     # Só vai mostrar posts com o check em publicar
        qs = qs.annotate(
            numero_comentarios=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        )  # ordenando de forma decrescente
        return qs


class PostBusca(PostIndex):  # Procura o post ao pesquisar
    template_name = 'posts/post_busca.html'
    # Sobrescrevendo o template_name da class Postindex para o html de busca

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')   # Pega o que foi digitado na busca

        if not termo:
            return qs

        qs = qs.filter(     # Serve para filtrar pela busca, verificando se contem o termo.
            Q(titulo_post__icontains=termo) |
            Q(autor_post__first_name__iexact=termo) |   # usa iexact pois autor_post é um ForeignKey
            Q(conteudo_post__icontains=termo) |
            Q(excerto_post__icontains=termo) |
            Q(categoria_post__nome_cat__iexact=termo)
        )

        return qs




class PostCategoria(PostIndex):
    template_name = 'posts/post_categoria.html'
    # Sobrescrevendo o template_name da class Postindex para o html de categoria

    def get_queryset(self):  # altera o modo de visualização dos posts
        qs = super().get_queryset()
        categoria = self.kwargs.get('categoria', None)  # Pega a categoria selecionada

        if not categoria:
            return qs

        qs = qs.filter(categoria_post__nome_cat__iexact=categoria)
        # Filtra os posts pela categoria e só mostra a selecionada
        # Na categoria_post, pega o nome_cat e veja se é igual a categoria

        return qs


class PostDetalhes(UpdateView):
    template_name = 'posts/post_detalhes.html'
    model = Post
    form_class = FormComentario
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        post = self.get_object()
        comentarios = Comentario.objects.filter(
            publicado_comentario=True, post_comentario=post.id,
        )
        contexto['comentarios'] = comentarios

        return contexto

    def form_valid(self, form):
        post = self.get_object()
        comentario = Comentario(**form.cleaned_data)
        comentario.post_comentario = post

        if self.request.user.is_authenticated:  # Verificando se o usuario está logado
            comentario.usuario_comentario = self.request.user

        comentario.save()

        messages.success(self.request, 'Comentário enviado com sucesso')

        return redirect('post_detalhes', pk=post.id)



