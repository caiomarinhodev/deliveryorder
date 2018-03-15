from django.views.generic import ListView, DetailView

from app.models import Estabelecimento, Produto


class HomeView(ListView):
    template_name = 'loja/index.html'
    context_object_name = 'lojas'
    model = Estabelecimento

    def get_queryset(self):
        return Estabelecimento.objects.all()


class LojaProdutosListView(DetailView):
    template_name = 'loja/view_produtos.html'
    context_object_name = 'loja'
    model = Estabelecimento
    pk_url_kwarg = 'pk'
