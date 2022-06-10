from django.forms import ModelForm
from . models import Comentario


class FormComentario(ModelForm):
    def clean(self):
        data = self.cleaned_data
        nome = data.get('nome_comentario')  # Pega o que foi digitado no campo nome
        email = data.get('nome_email')
        comentario = data.get('nome_comentario')

        # Validação do preenchimento dos comentários
        if len(nome) < 5:
            self.add_error(     # Vai criar o alerta vermelho em cima do campo
                'nome_comentario',
                'nome precisa ter mais que 5 caracteres'
            )

        if not comentario:
            self.add_error(  # Vai criar o alerta vermelho em cima do campo
                'nome_comentario',
                'nome precisa ter mais que 5 caracteres'
            )

    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')

