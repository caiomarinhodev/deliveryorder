from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from app.models import FormaEntrega
from app.views.mixins.Mixin import FocusMixin


class FormaEntregaListView(LoginRequiredMixin, ListView, FocusMixin):
    template_name = ''
    login_url = '/painel/login'
    context_object_name = 'formaentregas'
    model = FormaEntrega
    ordering = '-created_at'

    def get_queryset(self):
        est = self.request.user.estabelecimento
        return FormaEntrega.objects.filter(estabelecimento=est)


class FormaEntregaCreateView(LoginRequiredMixin, CreateView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'formaentrega'
    model = FormaEntrega
    success_url = '/formaentrega/list'
    template_name = ''
    # form_class = FormaEntregaForm


class FormaEntregaUpdateView(LoginRequiredMixin, UpdateView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'formaentrega'
    model = FormaEntrega
    success_url = '/formaentrega/list'
    template_name = ''
    # form_class = FormaEntregaForm


class FormaEntregaDeleteView(LoginRequiredMixin, DeleteView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'formaentrega'
    model = FormaEntrega
    success_url = '/formaentrega/list'
    template_name = ''


class FormaEntregaDetailView(LoginRequiredMixin, DetailView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'formaentrega'
    model = FormaEntrega
    template_name = ''
