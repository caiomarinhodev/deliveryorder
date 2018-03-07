#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
from django.views.generic import RedirectView

from app.forms import FormLogin
from app.models import *

__author__ = "Caio Marinho"
__copyright__ = "Copyright 2017"


class LojaRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user:
            try:
                loja = Estabelecimento.objects.get(user=self.request.user)
                if loja:
                    print ('--------- estabelecimento is logged')
                    return '/painel/'
            except:
                return '/login'
        else:
            return '/login'


class LojaLoginView(FormView):
    template_name = ''
    form_class = FormLogin
    success_url = '/painel'

    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(**data)
        print(user)
        if user is not None:
            login(self.request, user)
        else:
            return self.form_invalid(form)
        return super(LojaLoginView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Nenhum usuário encontrado')
        return super(LojaLoginView, self).form_invalid(form)


class LojaLogoutView(RedirectView):
    url = '/'
    permanent = False

    def get(self, request, *args, **kwargs):
        user = self.request.user
        loja = user.estabelecimento
        if loja:
            loja.is_online = False
            loja.save()
        logout(self.request)
        return super(LojaLogoutView, self).get(request, *args, **kwargs)
