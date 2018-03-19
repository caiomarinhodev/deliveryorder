#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import redirect

from app.models import ItemPedido, Opcional, OpcionalChoice, Cliente, Pedido, Estabelecimento, Produto


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
            obrigatorios = produto.grupo_set.filter(obrigatoriedade=True)
            if check_required_selected(checks, obrigatorios):
                obs = request.POST['observacoes']
                cria_item_pedido(checks, pedido, produto, obs)
            else:
                messages.error(request, u'Você deve selecionar 1 item das opcoes com *(asterisco)')
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
    id_loja = pedido.estabelecimento.id
    print(request.session)
    del request.session['pedido']
    print(request.session)
    pedido.delete()
    messages.success(request, 'Pedido deletado com sucesso')
    return redirect('/loja/'+str(id_loja))  # redirecionar para a loja


def check_required_selected(checks, list):
    for group in list:
        if group:
            for check in checks:
                opc = Opcional.objects.filter(id=check).first()
                if opc.grupo.id == group.id:
                    return True
            return False
        else:
            return True

