#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from app.models import Estabelecimento, Produto, Opcional, ItemPedido, OpcionalChoice, Pedido, Cliente
from app.views.mixins.Mixin import LojaFocusMixin


class HomeView(ListView, LojaFocusMixin):
    template_name = 'loja/index.html'
    context_object_name = 'lojas'
    model = Estabelecimento

    def get_queryset(self):
        return Estabelecimento.objects.all()


class LojaProdutosListView(DetailView, LojaFocusMixin):
    template_name = 'loja/view_produtos.html'
    context_object_name = 'loja'
    model = Estabelecimento
    pk_url_kwarg = 'pk'


def check_same_store(id_loja, pedido):
    if int(id_loja) == int(pedido.estabelecimento.id):
        return True
    return False


def cria_item_pedido(checks, pedido, produto, obs):
    itempedido = ItemPedido(pedido=pedido, quantidade='1', produto=produto, observacoes=obs)
    itempedido.save()
    for id in checks:
        opc = Opcional.objects.get(id=id)
        print(u'%s' % opc)
        opcc = OpcionalChoice(opcional=opc, item_pedido=itempedido)
        opcc.save()
    itempedido.save()


def is_logged(request):
    try:
        if request.user:
            cliente = Cliente.objects.get(usuario=request.user)
            if cliente:
                return True
            else:
                return False
        else:
            return False
    except (Exception,):
        return False


def get_pedido(request, id_loja):
    try:
        return Pedido.objects.get(id=request.session['pedido'])
    except (Exception,):
        estabelecimento = Estabelecimento.objects.get(id=id_loja)
        pedido = Pedido(cliente=request.user.cliente, estabelecimento=estabelecimento)
        pedido.save()
        request.session['pedido'] = pedido.id
        print('SESSION PEDIDO: ' + str(request.session['pedido']))
        return pedido


def add_cart(request, id_loja):
    print('loja: ' + str(id_loja))
    if is_logged(request):
        checks = request.POST.getlist('checks')
        print('--------------')
        pedido = get_pedido(request, id_loja)
        print('teste: ' + str(pedido.estabelecimento.id))
        print('check: ' + str(check_same_store(id_loja, pedido)))
        print('produton in : ' + str('produto' in request.POST))
        if check_same_store(id_loja, pedido) and ('produto' in request.POST):
            produto = Produto.objects.get(id=request.POST['produto'])
            obs = request.POST['observacoes']
            cria_item_pedido(checks, pedido, produto, obs)
        else:
            messages.error(request, u'Você deve comprar produtos no mesmo estabelecimento')
            return redirect('/loja/' + str(pedido.estabelecimento.id))
        pedido.save()
        print('loja: ' + str(id_loja))
        return redirect('/loja/' + str(pedido.estabelecimento.id))
    messages.error(request, u'Para fazer um pedido você deve estar logado')
    return redirect('/define/login')


def remove_cart(request, pk):
    pedido = Pedido.objects.get(id=request.session['pedido'])
    print(request.session)
    del request.session['pedido']
    print(request.session)
    pedido.delete()
    messages.success(request, 'Pedido deletado com sucesso')
    return redirect('/')  # redirecionar para a loja

# Refactor HomeView (10min)
# Implementar check na obrigatoriedade no backend (20min)
# Implementar Sistema para ficar ONLINE/OFFLINE (30min)
# Implementar JS check de obrigatoriedade no grupo  (15min)
# Implementar botao para Finalizar Pedido (10 min)
# Implementar tela de inserir dados de entrega,  (1h30)

# Implementar Notificacao de Pedido para Loja (painel)  (1h30)

# Implementar tela de Acompanhar Pedido. (2h)
# Implementar Aceitar, Rejeitar Pedido com set na tela de acompanhar pedido (2h)
# Implementar Lançamento de Pedido para Focus Geral (3h30)
# Implementar Alerta na Cozinha da Focus Geral (2h)

# Implementar Relatorios Simples para a Loja, de Vendas (2h)
# Implementar Configuracao de Loja (1h)
# Implementar Check de enviar pedido se e sommente se loja ONLINE. (10min)
# Implementar Random na vitrine de lojas Online (1h)

# ---------------------------------------
# Apos as sucessivas adicoes no carrinho, o cliente vai para a tela de inserir dados de entrega,
# completa o pedido e envia -> tela de acompanhar pedido
# notificar loja, e aceitacao e rejeicao atualizar tela de acompanhar pedido.
# limpar sessao, no fim;

# As Lojas tem Configuracao na Focus. Se possui conta no Geral (lança pedido no sistema e pra
# COZINHA), Private.
# Em Configuração, deve haver Tempo de preparo. Endereço da Loja. Telefone. CNPJ.
# DEVE HAVER NO DASHBOARD UM BOTAO PARA FICAR ONLINE E OFFLINE;

# O botao de enviar pedido só deve aparecer se a loja estiver ONLINE

# Implementar a notificacao do Motoboy, placa e informacoes dele para o Cliente que pediu. (8h)

# Implementar API
