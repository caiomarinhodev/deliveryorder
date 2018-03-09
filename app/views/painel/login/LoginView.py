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
    template_name = 'painel/login.html'
    form_class = FormLogin

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

    def get_success_url(self):
        """
        Returns the supplied URL.
        """
        url = '/login'
        try:
            loja = self.request.user.estabelecimento
        except:
            loja = None

        if loja:
            url = '/dashboard'
            loja.is_online = True
            loja.save()
            self.success_url = url
        return url


class LojaLogoutView(RedirectView):
    url = '/login'
    permanent = False

    def get(self, request, *args, **kwargs):
        user = self.request.user
        loja = user.estabelecimento
        if loja:
            loja.is_online = False
            loja.save()
        logout(self.request)
        return super(LojaLogoutView, self).get(request, *args, **kwargs)
