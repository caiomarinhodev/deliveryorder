from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from app.forms import FormOpcional
from app.models import Opcional
from app.views.mixins.Mixin import FocusMixin


class OpcionalListView(LoginRequiredMixin, ListView, FocusMixin):
    template_name = 'painel/opcional/list.html'
    login_url = '/painel/login'
    context_object_name = 'opcionais'
    model = Opcional
    ordering = '-created_at'

    def get_queryset(self):
        est = self.request.user.estabelecimento
        return Opcional.objects.filter(produto__categoria__estabelecimento=est)


class OpcionalCreateView(LoginRequiredMixin, CreateView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'opcional'
    model = Opcional
    success_url = '/opcional/list'
    template_name = 'painel/opcional/add.html'
    form_class = FormOpcional


class OpcionalUpdateView(LoginRequiredMixin, UpdateView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'opcional'
    model = Opcional
    success_url = '/opcional/list'
    template_name = 'painel/opcional/edit.html'
    form_class = FormOpcional


class OpcionalDeleteView(LoginRequiredMixin, DeleteView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'opcional'
    model = Opcional
    success_url = '/opcional/list'
    template_name = 'painel/opcional/delete.html'
