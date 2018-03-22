from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import Context
from django.views.decorators.http import require_http_methods

from app.models import Notificacao, Pedido
from app.views.snippet_template import render_block_to_string


@require_http_methods(["GET"])
def notificacao_pedido(request):
    notificacao = Notificacao.objects.filter(to=request.user, type_message='NOVO_PEDIDO', is_read=False).last()
    context = Context({'notificacao': notificacao, 'user': request.user})
    return_str = render_block_to_string('painel/includes/notificacao.html', context)
    # Nao marcar como lido. Marcar somente depois que aceitar ou rejeitar.
    # if notificacao:
    #     notificacao.is_read = True
    #     notificacao.save()
    return HttpResponse(return_str)


def mark_read(request):
    notificacao = Notificacao.objects.filter(to=request.user, type_message='NOVO_PEDIDO', is_read=False).last()
    if notificacao:
        notificacao.is_read = True
        notificacao.save()


def aceitar_pedido(request, pk):
    mark_read(request)
    pedido = Pedido.objects.get(id=pk)
    pedido.status_pedido = 'ACEITO'
    pedido.save()
    return redirect('/dashboard')


def rejeitar_pedido(request, pk):
    mark_read(request)
    pedido = Pedido.objects.get(id=pk)
    pedido.status_pedido = 'REJEITADO'
    pedido.save()
    return redirect('/dashboard')
