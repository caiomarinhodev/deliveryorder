from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from app.models import Categoria, Classificacao
from app.views.mixins.Mixin import FocusMixin


class ClassificacaoListView(LoginRequiredMixin, ListView, FocusMixin):
    template_name = 'painel/classificacao/list.html'
    login_url = '/painel/login'
    context_object_name = 'classificacoes'
    model = Classificacao
    ordering = '-created_at'

    def get_queryset(self):
        est = self.request.user.estabelecimento
        return Classificacao.objects.filter(pedido__estabelecimento=est)
