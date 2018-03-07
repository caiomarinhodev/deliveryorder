#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from app.models import Pedido
from app.views.mixins.Mixin import FocusMixin

"""HomeView.py: Especifica a pagina inicial da aplicacao."""

__author__ = "Caio Marinho"
__copyright__ = "Copyright 2017"


class DashboardPedidosListView(LoginRequiredMixin, ListView, FocusMixin):
    login_url = '/login/'
    template_name = ''
    model = Pedido
    context_object_name = 'pedidos'

    def get_queryset(self):
        return Pedido.objects.filter(estabelecimento=self.request.user.estabelecimento).order_by('-created_at')
