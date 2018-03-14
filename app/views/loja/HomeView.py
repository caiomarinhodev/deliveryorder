from django.views.generic import ListView, DetailView

from app.models import Estabelecimento, Produto


class HomeView(ListView):
    template_name = 'loja/index.html'
    context_object_name = 'lojas'
    model = Estabelecimento

    def get_queryset(self):
        return Estabelecimento.objects.all()


class ProdutoDetailView(DetailView):
    template_name = ''
    context_object_name = 'loja'
    model = Estabelecimento
