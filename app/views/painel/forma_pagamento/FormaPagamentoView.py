from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from app.models import FormaPagamento
from app.views.mixins.Mixin import FocusMixin


class FormaPagamentoListView(LoginRequiredMixin, ListView, FocusMixin):
    template_name = ''
    login_url = '/painel/login'
    context_object_name = 'formapagamentos'
    model = FormaPagamento
    ordering = '-created_at'

    def get_queryset(self):
        est = self.request.user.estabelecimento
        return FormaPagamento.objects.filter(estabelecimento=est)


class FormaPagamentoCreateView(LoginRequiredMixin, CreateView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'formapagamento'
    model = FormaPagamento
    success_url = '/formapagamento/list'
    template_name = ''
    # form_class = FormaPagamentoForm


class FormaPagamentoUpdateView(LoginRequiredMixin, UpdateView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'formapagamento'
    model = FormaPagamento
    success_url = '/formapagamento/list'
    template_name = ''
    # form_class = FormaPagamentoForm


class FormaPagamentoDeleteView(LoginRequiredMixin, DeleteView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'formapagamento'
    model = FormaPagamento
    success_url = '/formapagamento/list'
    template_name = ''


class FormaPagamentoDetailView(LoginRequiredMixin, DetailView, FocusMixin):
    login_url = '/painel/login'
    context_object_name = 'formapagamento'
    model = FormaPagamento
    template_name = ''
