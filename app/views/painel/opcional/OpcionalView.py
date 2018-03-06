from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from app.models import Opcional
from app.views.mixins.Mixin import FocusMixin


class OpcionalListView(LoginRequiredMixin, ListView, FocusMixin):
    template_name = ''
    login_url = '/painel/login'
    context_object_name = 'opcionais'
    model = Opcional
    ordering = '-created_at'

    def get_queryset(self):
        est = self.request.user.estabelecimento
        return Opcional.objects.filter(estabelecimento=est)


class OpcionalCreateView(LoginRequiredMixin, CreateView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'opcional'
    model = Opcional
    success_url = '/opcional/list'
    template_name = ''
    # form_class = OpcionalForm


class OpcionalUpdateView(LoginRequiredMixin, UpdateView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'opcional'
    model = Opcional
    success_url = '/opcional/list'
    template_name = ''
    # form_class = OpcionalForm


class OpcionalDeleteView(LoginRequiredMixin, DeleteView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'opcional'
    model = Opcional
    success_url = '/opcional/list'
    template_name = ''


class OpcionalDetailView(LoginRequiredMixin, DetailView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'opcional'
    model = Opcional
    template_name = ''
