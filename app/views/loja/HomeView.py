#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from app.models import Estabelecimento, Produto, Opcional


class HomeView(ListView):
    template_name = 'loja/index.html'
    context_object_name = 'lojas'
    model = Estabelecimento

    def get_queryset(self):
        return Estabelecimento.objects.all()


class LojaProdutosListView(DetailView):
    template_name = 'loja/view_produtos.html'
    context_object_name = 'loja'
    model = Estabelecimento
    pk_url_kwarg = 'pk'


def add_cart(request, id_loja):
    # verifica se esta logado,
    # se sim get_pedido(),
    # se sim cria itempedido, um ou mais OpcChoice, e save novamente em itemPedido
    # se nao.. login/registro.
    print('loja: '+str(id_loja))
    if is_logged(request):
        checks = request.POST.getlist('checks')
        print('--------------')
        # checar se esta comprando da mesma loja, vendo o estabelecimento da request e o estabelecimento do pedido.
        # checar se produto id esta presente no form, se nao messages e redirect
        # checar se checks(opcionais) nao eh vazio, se sim messages e redirect
        for id in checks:
            opc = Opcional.objects.get(id=id)
            print(u'%s' % opc)
        print('--------------')
        print('Produto id: ' + str(request.POST['produto']))
        print(Produto.objects.get(id=request.POST['produto']))
        return redirect('/loja/1/')
    messages.error(request, u'Para pedir você deve estar logado')
    return redirect('/define/login')


def is_logged(request):
    try:
        if request.user.cliente:
            return True
        else:
            return False
    except (Exception,):
        return False


def get_pedido(request):
    # verifica se ja existe pedido existente na sessao, else
    # cria pedido com cliente-estabelecimento
    # request.session['pedido'] = pedido.id #passa o id para a sessao
    pass


# Apos as sucessivas adicoes no carrinho, o cliente vai para a tela de inserir dados de entrega,
# completa o pedido e envia -> tela de acompanhar pedido
# notificar loja, e aceitacao e rejeicao atualizar tela de acompanhar pedido.
# limpar sessao, no fim;


# As Lojas tem Configuracao na Focus. Se possui conta no Geral (lança pedido no sistema e pra
# COZINHA), Private.
# Em Configuração, deve haver Tempo de preparo. Endereço da Loja. Telefone. CNPJ.
# DEVE HAVER NO DASHBOARD UM BOTAO PARA FICAR ONLINE E OFFLINE;
