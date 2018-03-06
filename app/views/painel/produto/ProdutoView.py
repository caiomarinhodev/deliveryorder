from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from app.models import Produto
from app.views.mixins.Mixin import FocusMixin


class ProdutoListView(LoginRequiredMixin, ListView, FocusMixin):
    template_name = ''
    login_url = '/painel/login'
    context_object_name = 'produtos'
    model = Produto
    ordering = '-created_at'

    def get_queryset(self):
        est = self.request.user.estabelecimento
        return Produto.objects.filter(estabelecimento=est)


class ProdutoCreateView(LoginRequiredMixin, CreateView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'produto'
    model = Produto
    success_url = '/produto/list'
    template_name = ''
    # form_class = ProdutoForm


class ProdutoUpdateView(LoginRequiredMixin, UpdateView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'produto'
    model = Produto
    success_url = '/produto/list'
    template_name = ''
    # form_class = ProdutoForm


class ProdutoDeleteView(LoginRequiredMixin, DeleteView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'produto'
    model = Produto
    success_url = '/produto/list'
    template_name = ''


class ProdutoDetailView(LoginRequiredMixin, DetailView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'produto'
    model = Produto
    template_name = ''
