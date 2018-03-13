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

from app.views.painel.dashboard.DashboardView import DashboardPedidosListView
from app.views.painel.login.LoginView import LojaLoginView, LojaLogoutView
from app.views.painel.categoria.CategoriaView import *

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
    # url(r'^$', AppView.as_view(), name='home'),
]
