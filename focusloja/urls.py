"""focusloja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from app.views.loja.CarrinhoView import add_cart, FinalizaPedido, submit_pedido
from app.views.loja.CarrinhoView import remove_cart
from app.views.loja.LoginView import *
from app.views.painel.dashboard.DashboardView import DashboardPedidosListView
from app.views.painel.login.LoginView import LojaLoginView, LojaLogoutView
from app.views.painel.categoria.CategoriaView import *
from app.views.painel.produto.ProdutoView import *
from app.views.painel.opcional.OpcionalView import *
from app.views.painel.foto_produto.FotoProdutoView import *
from app.views.painel.forma_pagamento.FormaPagamentoView import *
from app.views.painel.forma_entrega.FormaEntregaView import *
from app.views.painel.classificacao.ClassificacaoView import *
from app.views.painel.notificacao.NotificacaoView import *
from app.views.painel.grupo.GrupoView import *
from app.views.loja.HomeView import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/login/$', auth_views.login),

    url(r'^login/$', LojaLoginView.as_view(), name='login'),
    url(r'^logout/$', LojaLogoutView.as_view(), name='auth_logout'),
    url(r'^dashboard/$', DashboardPedidosListView.as_view(), name='dashboard'),

    url(r'^categoria/add/$', CategoriaCreateView.as_view(), name='add_categoria'),
    url(r'^categoria/edit/(?P<pk>[0-9]+)/$', CategoriaUpdateView.as_view(), name='edit_categoria'),
    url(r'^categoria/list/$', CategoriaListView.as_view(), name='list_categoria'),
    url(r'^categoria/delete/(?P<pk>[0-9]+)/$', CategoriaDeleteView.as_view(), name='delete_categoria'),

    url(r'^produto/add/$', ProdutoCreateView.as_view(), name='add_produto'),
    url(r'^produto/edit/(?P<pk>[0-9]+)/$', ProdutoUpdateView.as_view(), name='edit_produto'),
    url(r'^produto/list/$', ProdutoListView.as_view(), name='list_produto'),
    url(r'^produto/delete/(?P<pk>[0-9]+)/$', ProdutoDeleteView.as_view(), name='delete_produto'),

    url(r'^grupo/add/$', GrupoCreateView.as_view(), name='add_grupo'),
    url(r'^grupo/edit/(?P<pk>[0-9]+)/$', GrupoUpdateView.as_view(), name='edit_grupo'),
    url(r'^grupo/list/$', GrupoListView.as_view(), name='list_grupo'),
    url(r'^grupo/delete/(?P<pk>[0-9]+)/$', GrupoDeleteView.as_view(), name='delete_grupo'),

    url(r'^opcional/add/$', OpcionalCreateView.as_view(), name='add_opcional'),
    url(r'^opcional/edit/(?P<pk>[0-9]+)/$', OpcionalUpdateView.as_view(), name='edit_opcional'),
    url(r'^opcional/list/$', OpcionalListView.as_view(), name='list_opcional'),
    url(r'^opcional/delete/(?P<pk>[0-9]+)/$', OpcionalDeleteView.as_view(), name='delete_opcional'),

    url(r'^foto/add/$', FotoProdutoCreateView.as_view(), name='add_foto'),
    url(r'^foto/edit/(?P<pk>[0-9]+)/$', FotoProdutoUpdateView.as_view(), name='edit_foto'),
    url(r'^foto/list/$', FotoProdutoListView.as_view(), name='list_foto'),
    url(r'^foto/delete/(?P<pk>[0-9]+)/$', FotoProdutoDeleteView.as_view(), name='delete_foto'),

    url(r'^pagamento/add/$', FormaPagamentoCreateView.as_view(), name='add_pagamento'),
    url(r'^pagamento/edit/(?P<pk>[0-9]+)/$', FormaPagamentoUpdateView.as_view(), name='edit_pagamento'),
    url(r'^pagamento/list/$', FormaPagamentoListView.as_view(), name='list_pagamento'),
    url(r'^pagamento/delete/(?P<pk>[0-9]+)/$', FormaPagamentoDeleteView.as_view(), name='delete_pagamento'),

    url(r'^entrega/add/$', FormaEntregaCreateView.as_view(), name='add_entrega'),
    url(r'^entrega/edit/(?P<pk>[0-9]+)/$', FormaEntregaUpdateView.as_view(), name='edit_entrega'),
    url(r'^entrega/list/$', FormaEntregaListView.as_view(), name='list_entrega'),
    url(r'^entrega/delete/(?P<pk>[0-9]+)/$', FormaEntregaDeleteView.as_view(), name='delete_entrega'),

    url(r'^classificacao/list/$', ClassificacaoListView.as_view(), name='list_classificacao'),

    url(r'^notificacao/list/$', NotificacaoListView.as_view(), name='list_notificacao'),

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^loja/(?P<pk>[0-9]+)/$', LojaProdutosListView.as_view(), name='view_loja'),

    url(r'^define/login/$', EscolheLoginView.as_view(), name='choose_login'),
    url(r'^login/cliente/$', ClienteLoginView.as_view(), name='login_cliente'),
    url(r'^registro/cliente', RegistroCliente.as_view(), name='registro_cliente'),
    # url(r'^$', AppView.as_view(), name='home'),

    url(r'^add-cart/(?P<id_loja>[0-9]+)/$', add_cart, name='add_cart'),

    url(r'^delete-pedido/(?P<pk>[0-9]+)/$', remove_cart, name='delete_pedido'),

    url(r'set-online/$', SetOnlineView.as_view(), name='set_online'),

    url(r'finaliza-pedido/$', FinalizaPedido.as_view(), name='finaliza_pedido'),

    url(r'submit-pedido/$', submit_pedido, name='submit_pedido'),

    url(r'^script/bairro/$', script, name='script_bairro'),

]
