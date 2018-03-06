# coding=utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from app.views.geocoding import geocode


class TimeStamped(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)


class Bairro(TimeStamped):
    nome = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return u'%s' % self.nome

    def __str__(self):
        return u'%s' % self.nome


class BaseAddress(models.Model):
    class Meta:
        abstract = True

    bairro = models.ForeignKey(Bairro, blank=True, null=True, verbose_name='Bairro')
    endereco = models.CharField(max_length=200, blank=True, null=True, verbose_name='Endereço')
    numero = models.CharField(max_length=5, blank=True, null=True, verbose_name='Número')
    complemento = models.CharField(max_length=300, blank=True, null=True, verbose_name='Ponto de Referência')
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)


THEMES = (
    ('BLACK', 'skin-black'),
    ('BLUE', 'skin-blue'),
    ('RED', 'skin-red'),
    ('YELLOW', 'skin-yellow'),
    ('PURPLE', 'skin-purple'),
    ('GREEN', 'skin-green'),
    # 'skin-blue-light',
    # 'skin-black-light',
    # 'skin-red-light',
    # 'skin-yellow-light',
    # 'skin-purple-light',
    # 'skin-green-light'
)

PLANS = (
    ('BASIC', 'BASIC'),
    ('PREMIUM', 'PREMIUM'),
)


class Cliente(TimeStamped, BaseAddress):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    cpf = models.CharField(max_length=100, blank=True, null=True, default="", unique=True)
    foto = models.URLField(blank=True, null=True, default="http://placehold.it/100x100")
    telefone = models.CharField(max_length=30, blank=True, null=True)
    is_online = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        try:
            endereco = self.endereco + ", " + self.numero + ",Campina Grande,PB"
            pto = geocode(endereco)
            self.lat = pto['latitude']
            self.lng = pto['longitude']
        except (Exception,):
            pass
        super(Cliente, self).save(*args, **kwargs)

    def __str__(self):
        return u'%s %s' % (self.usuario.first_name, self.usuario.last_name)

    def __unicode__(self):
        return u'%s %s' % (self.usuario.first_name, self.usuario.last_name)


class Estabelecimento(TimeStamped, BaseAddress):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    foto = models.URLField(blank=True, null=True, default="http://placehold.it/100x100")
    telefone = models.CharField(max_length=30, blank=True)
    is_online = models.BooleanField(default=False)
    endereco_completo = models.CharField(max_length=300, blank=True, null=True)

    def save(self, *args, **kwargs):
        try:
            self.numero = self.numero.replace("_", "")
            self.fone = self.fone.replace("_", "")
            endereco = self.endereco + ", " + self.numero + ",Campina Grande,PB"
            self.endereco_completo = endereco
            pto = geocode(endereco)
            self.lat = pto['latitude']
            self.lng = pto['longitude']
        except (Exception,):
            pass
        super(Estabelecimento, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s %s' % (self.usuario.first_name, self.usuario.last_name)

    def __str__(self):
        return u'%s %s' % (self.usuario.first_name, self.usuario.last_name)

    # class Meta:
    #     permissions = (
    #         ("view_dashboard_1", "Loja pode ver o dashboard loja tipo 1"),
    #         ("view_dashboard_2", "Loja pode ver o dashboard loja tipo 2"),
    #         ("view_dashboard_3", "Loja pode ver o dashboard loja tipo 3"),
    #         ("view_chat", "Loja pode interagir no Chat"),
    #     )


STATUS = (
    ('AGUARDANDO', 'AGUARDANDO'),
    ('PREPARANDO', 'PREPARANDO'),
    ('ENTREGANDO', 'ENTREGANDO'),
    ('ENTREGUE', 'ENTREGUE'),
)


class Categoria(TimeStamped):
    estabelecimento = models.ForeignKey(Estabelecimento)
    nome = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.nome

    def __str__(self):
        return u'%s' % self.nome


class Produto(TimeStamped):
    nome = models.CharField(max_length=100)
    preco_base = models.CharField(max_length=10)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s' % self.nome

    def __str__(self):
        return u'%s' % self.nome


class Opcional(TimeStamped):
    nome = models.CharField(max_length=100)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.CharField(max_length=10)

    def __unicode__(self):
        return u'%s' % self.nome

    def __str__(self):
        return u'%s' % self.nome


class FotoProduto(TimeStamped):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    url = models.URLField(blank=True, null=True, default="http://placehold.it/200x200")

    def __unicode__(self):
        return u'%s' % self.url

    def __str__(self):
        return u'%s' % self.url


TIPOS_PAGAMENTO = (
    ('CREDITO', 'CREDITO'),
    ('DEBITO', 'DEBITO'),
    ('DINHEIRO', 'DINHEIRO'),
    ('REFEICAO', 'REFEICAO'),
)

TIPOS_CARTAO = (
    ('MASTERCARD', 'MASTERCARD'),
    ('VISA', 'VISA'),
    ('ELO', 'ELO'),
    ('VR', 'VR'),
    ('HIPERCARD', 'HIPERCARD'),
    ('SODEXO', 'SODEXO'),
)


class FormaPagamento(TimeStamped):
    forma = models.CharField(max_length=100, choices=TIPOS_PAGAMENTO, blank=True, null=True, default="DINHEIRO")
    cartao = models.CharField(max_length=100, choices=TIPOS_CARTAO, blank=True, null=True)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s' % self.forma

    def __str__(self):
        return u'%s' % self.forma


TIPOS_ENTREGA = (
    ('VOU BUSCAR', 'VOU BUSCAR'),
    ('MOTOBOY', 'MOTOBOY'),
)


class FormaEntrega(TimeStamped):
    forma = models.CharField(max_length=100, choices=TIPOS_ENTREGA, blank=True, null=True, default="MOTOBOY")
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s' % self.forma

    def __str__(self):
        return u'%s' % self.forma


class Pedido(TimeStamped):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    status_pedido = models.CharField(max_length=100, choices=STATUS, blank=True, null=True, default='AGUARDANDO')
    valor_total = models.CharField(max_length=10)
    troco = models.CharField(max_length=10)
    forma_pagamento = models.ForeignKey(FormaPagamento, blank=True, null=True, on_delete=models.CASCADE)
    forma_entrega = models.ForeignKey(FormaEntrega, blank=True, null=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s - %s - %s - %s' % (self.id, self.cliente, self.estabelecimento, self.valor_total)

    def __str__(self):
        return u'%s - %s - %s - %s' % (self.id, self.cliente, self.estabelecimento, self.valor_total)

    def save(self, *args, **kwargs):
        valor = 0.0
        for item in self.itempedido_set.all():
            valor = float(valor) + float(item.valor_total)
        self.valor_total = float(valor)
        super(Pedido, self).save(*args, **kwargs)


class ItemPedido(TimeStamped):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto)
    quantidade = models.CharField(max_length=10, blank=True, null=True, default="1")
    observacoes = models.TextField(blank=True, null=True)
    valor_total = models.CharField(max_length=10, blank=True, null=True)

    def save(self, *args, **kwargs):
        valor_base = float(self.produto.preco_base)
        valor_opcionais = 0.0
        for opc in self.opcionalchoice_set.all():
            valor_opcionais = float(valor_opcionais) + float(opc.opcional.valor)
        valor_unitario = float(valor_base) + float(valor_opcionais)
        self.valor_total = float(float(valor_unitario) * float(self.quantidade))
        super(ItemPedido, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s - %s - %s' % (self.pedido.id, self.produto, self.quantidade)

    def __str__(self):
        return u'%s - %s - %s' % (self.pedido.id, self.produto, self.quantidade)


class OpcionalChoice(TimeStamped):
    opcional = models.ForeignKey(Opcional, on_delete=models.CASCADE)
    item_pedido = models.ForeignKey(ItemPedido)

    def __unicode__(self):
        return u'%s' % self.opcional

    def __str__(self):
        return u'%s' % self.opcional


type_notification = (
    ('NOVO_PEDIDO', 'NOVO_PEDIDO'),
    ('ADMIN_MESSAGE', 'ADMIN_MESSAGE'),
)


class Notificacao(TimeStamped):
    message = models.TextField()
    to = models.ForeignKey(User, on_delete=models.CASCADE)
    type_message = models.CharField(choices=type_notification, max_length=100)
    is_read = models.BooleanField(default=False)

    def __unicode__(self):
        return u'Para: %s' % self.to

    def __str__(self):
        return u'Para: %s' % self.to


class Mensagem(TimeStamped):
    u_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='u_from')
    u_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='u_to')
    text = models.TextField()
    is_read = models.BooleanField(default=False)

    def __unicode__(self):
        return u'De: %s Para: %s' % (self.u_from, self.u_to)

    def __str__(self):
        return u'De: %s Para: %s' % (self.u_from, self.u_to)


class Classificacao(TimeStamped):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    nota = models.CharField(max_length=2)

    def __unicode__(self):
        return u'Pedido:%s Nota:%s' % (self.pedido, self.nota)
    def __str__(self):
        return u'Pedido:%s Nota:%s' % (self.pedido, self.nota)
