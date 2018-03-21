from django.http import HttpResponse
from django.template import Context
from django.views.decorators.http import require_http_methods

from app.models import Notificacao
from app.views.snippet_template import render_block_to_string


@require_http_methods(["GET"])
def notificacao_pedido(request):
    notificacao = Notificacao.objects.filter(to=request.user, type_message='NOVO_PEDIDO', is_read=False).last()
    context = Context({'notificacao': notificacao, 'user': request.user})
    return_str = render_block_to_string('painel/includes/notificacao.html', context)
    # Nao marcar como lido. Marcar somente depois que aceitar ou rejeitar.
    if notificacao:
        notificacao.is_read = True
        notificacao.save()
    return HttpResponse(return_str)
