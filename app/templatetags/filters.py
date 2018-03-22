#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import time, datetime

from django import template

register = template.Library()


@register.filter
def divide(value, arg):
    try:
        return float(float(value) / float(arg))
    except (ValueError, ZeroDivisionError):
        return None


@register.filter
def is_madrugada(user):
    try:
        now_time = datetime.now().time()
        if time(22, 59) <= now_time <= time(23, 59):
            return True
        elif time(0, 00) <= now_time <= time(5, 59):
            return True
        return False
    except (ValueError, ZeroDivisionError, Exception):
        return 0


@register.filter
def get_itens(pedido):
    try:
        message = u''
        for it in pedido.itempedido_set.all():
            message += u' ' + unicode(it.produto.nome) + u'('
            for opc in it.opcionalchoice_set.all():
                message += unicode(opc.opcional.nome) + u','
            message += u') '
        return message
    except (Exception,):
        return u''
