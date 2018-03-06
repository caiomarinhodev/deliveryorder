from django.contrib import admin

from app.models import *

"""
admin.py: Definicao de classes para gerenciar no painel de admin do Django.
"""
__author__ = "Caio Marinho"
__copyright__ = "Copyright 2017"


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido


class OpcionalChoiceInline(admin.TabularInline):
    model = OpcionalChoice


class OpcionalChoiceAdmin(admin.ModelAdmin):
    list_display = ('opcional', 'item_pedido', 'created_at', 'id')


class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'pedido', 'produto', 'quantidade', 'valor_total', 'cliente', 'estabelecimento',)
    inlines = [OpcionalChoiceInline, ]

    def cliente(self, obj):
        return obj.pedido.cliente

    def estabelecimento(self, obj):
        return obj.pedido.estabelecimento


class FotoProdutoInline(admin.TabularInline):
    model = FotoProduto


class FotoProdutoAdmin(admin.ModelAdmin):
    list_display = ('url', 'produto', 'id', 'estabelecimento', 'created_at')

    def estabelecimento(self, obj):
        return obj.produto.categoria.estabelecimento


class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'usuario', 'qtd_pedidos', 'cpf', 'telefone', 'endereco', 'bairro', 'numero', 'email_cliente', 'is_online',
        'created_at')

    def email_cliente(self, obj):
        return obj.usuario.email

    def qtd_pedidos(self, obj):
        return obj.pedido_set.all()


class EstabelecimentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_loja', 'usuario', 'telefone', 'endereco_completo', 'is_online', 'created_at')

    def nome_loja(self, obj):
        return obj.usuario.first_name


class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInline,
    ]
    list_display = ('cliente', 'estabelecimento', 'status_pedido', 'valor_total', 'troco', 'id',
                    'forma_pagamento', 'forma_entrega', 'created_at')


class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'type_message', 'to', 'is_read')


class BairroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id', 'created_at')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id', 'estabelecimento', 'created_at',)


class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        FotoProdutoInline,
    ]
    list_display = ('nome', 'id', 'preco_base', 'categoria', 'created_at', 'estabelecimento')

    def estabelecimento(self, obj):
        return obj.categoria.estabelecimento


class MensagemAdmin(admin.ModelAdmin):
    list_display = ('u_from', 'u_to', 'id', 'is_read', 'created_at')


class ClassificacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'nota', 'cliente', 'estabelecimento',)

    def cliente(self, obj):
        return obj.pedido.cliente

    def estabelecimento(self, obj):
        return obj.pedido.estabelecimento


class FormaPagamentoAdmin(admin.ModelAdmin):
    list_display = ('forma', 'cartao', 'id', 'estabelecimento', 'created_at',)


class FormaEntregaAdmin(admin.ModelAdmin):
    list_display = ('forma', 'id', 'estabelecimento', 'created_at',)

class OpcionalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id', 'produto', 'valor', 'estabelecimento', 'created_at',)

    def estabelecimento(self, obj):
        return obj.produto.categoria.estabelecimento


admin.site.register(Classificacao, ClassificacaoAdmin)
admin.site.register(Estabelecimento, EstabelecimentoAdmin)
admin.site.register(ItemPedido, ItemPedidoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Notificacao, NotificacaoAdmin)
admin.site.register(Mensagem, MensagemAdmin)
admin.site.register(Bairro, BairroAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(FotoProduto, FotoProdutoAdmin)
admin.site.register(FormaPagamento, FormaPagamentoAdmin)
admin.site.register(FormaEntrega, FormaEntregaAdmin)
admin.site.register(OpcionalChoice, OpcionalChoiceAdmin)
admin.site.register(Opcional, OpcionalAdmin)