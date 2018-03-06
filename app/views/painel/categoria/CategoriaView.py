from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from app.models import Categoria
from app.views.mixins.Mixin import FocusMixin


class CategoriaListView(LoginRequiredMixin, ListView, FocusMixin):
    template_name = ''
    login_url = '/painel/login'
    context_object_name = 'categorias'
    model = Categoria
    ordering = '-created_at'

    def get_queryset(self):
        est = self.request.user.estabelecimento
        return Categoria.objects.filter(estabelecimento=est)


class CategoriaCreateView(LoginRequiredMixin, CreateView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'categoria'
    model = Categoria
    success_url = '/categoria/list'
    template_name = ''
    # form_class = CategoriaForm


class CategoriaUpdateView(LoginRequiredMixin, UpdateView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'categoria'
    model = Categoria
    success_url = '/categoria/list'
    template_name = ''
    # form_class = CategoriaForm


class CategoriaDeleteView(LoginRequiredMixin, DeleteView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'categoria'
    model = Categoria
    success_url = '/categoria/list'
    template_name = ''


class CategoriaDetailView(LoginRequiredMixin, DetailView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'categoria'
    model = Categoria
    template_name = ''
