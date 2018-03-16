#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, inlineformset_factory

from app.models import Pedido, Estabelecimento, Categoria, Produto, FotoProduto, Opcional, FormaPagamento, FormaEntrega, \
    Cliente


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'phone' or field_name == 'telefone':
                field.widget.attrs['class'] = 'form-control telefone'
            if field_name == 'numero' or field_name == 'number':
                field.widget.attrs['class'] = 'form-control numero'


class FormBaseAddress(BaseForm):
    cep = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'required': True,
                                                                       'maxlength': 200,
                                                                       'placeholder': 'CEP'
                                                                       }))
    endereco = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'required': True,
                                                                             'maxlength': 200,
                                                                             'placeholder': 'Endereço'
                                                                             }))
    numero = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'required': True,
                                                                         'maxlength': 200,
                                                                         'placeholder': 'Número'
                                                                         }))
    bairro = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'required': True,
                                                                          'maxlength': 200,
                                                                          'placeholder': 'Bairro'
                                                                          }))


class FormLogin(BaseForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                             'maxlength': 200,
                                                             'placeholder': 'Login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True,
                                                                 'placeholder': 'Senha'}))


class FormCategoria(ModelForm, BaseForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'estabelecimento', ]

    def __init__(self, *args, **kwargs):
        super(FormCategoria, self).__init__(*args, **kwargs)
        self.fields['estabelecimento'].widget.attrs['class'] = 'hidden'
        self.fields['estabelecimento'].label = ''


class FormProduto(ModelForm, BaseForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco_base', 'categoria']


class FormFotoProdutoInline(ModelForm, BaseForm):
    class Meta:
        model = FotoProduto
        fields = ['url', ]


class FormFotoProduto(ModelForm, BaseForm):
    class Meta:
        model = FotoProduto
        fields = ['url', 'produto', ]


class FormOpcionalInline(ModelForm, BaseForm):
    class Meta:
        model = Opcional
        fields = ['nome', 'valor', ]


class FormOpcional(ModelForm, BaseForm):
    class Meta:
        model = Opcional
        fields = ['nome', 'valor', 'produto', ]


FotoProdutoFormSet = inlineformset_factory(Produto, FotoProduto, form=FormFotoProdutoInline, extra=1)
OpcionalFormSet = inlineformset_factory(Produto, Opcional, form=FormOpcionalInline, extra=1)


class FormFormaPagamento(ModelForm, BaseForm):
    class Meta:
        model = FormaPagamento
        fields = ['forma', 'cartao', 'estabelecimento']

    def __init__(self, *args, **kwargs):
        super(FormFormaPagamento, self).__init__(*args, **kwargs)
        self.fields['estabelecimento'].widget.attrs['class'] = 'hidden'
        self.fields['estabelecimento'].label = ''


class FormFormaEntrega(ModelForm, BaseForm):
    class Meta:
        model = FormaEntrega
        fields = ['forma', 'estabelecimento', ]

    def __init__(self, *args, **kwargs):
        super(FormFormaEntrega, self).__init__(*args, **kwargs)
        self.fields['estabelecimento'].widget.attrs['class'] = 'hidden'
        self.fields['estabelecimento'].label = ''


class FormRegisterCliente(ModelForm, BaseForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                             'maxlength': 100,
                                                             'placeholder': 'Nome'}))
    sobrenome = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                             'maxlength': 100,
                                                             'placeholder': 'Sobrenome'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'required': True,
                                                                 'placeholder': 'Senha'}))
    class Meta:
        model = Cliente
        fields = ['cpf', 'telefone', 'usuario']

    def __init__(self, *args, **kwargs):
        super(FormRegisterCliente, self).__init__(*args, **kwargs)
        self.fields['usuario'].widget.attrs['class'] = 'hidden'
        self.fields['usuario'].label = ''


class FormLoginCliente(BaseForm):
    cpf = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                             'maxlength': 12,
                                                             'placeholder': 'CPF'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True,
                                                                 'placeholder': 'Senha'}))
#
# class FormPonto(ModelForm, BaseForm):
#     telefone = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class': 'telefone',
#                                                              'maxlength': 200,
#                                                              'placeholder': 'Telefone do Cliente'}))
#     cliente = forms.CharField(widget=forms.TextInput(attrs={'required': True,
#                                                             'maxlength': 200,
#                                                             'placeholder': 'Nome do Cliente'}))
#
#     endereco = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'required': True,
#                                                                              'maxlength': 200,
#                                                                              'placeholder': 'Endereço'
#                                                                              }))
#     numero = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'required': True,
#                                                                          'maxlength': 6, 'class': 'numero',
#                                                                          'placeholder': 'Número'
#                                                                          }))
#     complemento = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'required': True,
#                                                                                 'maxlength': 200,
#                                                                                 'placeholder': 'Ponto de Referencia'
#                                                                                 }))
#     observacoes = forms.CharField(required=False, max_length=300, widget=forms.Textarea(attrs={'required': True,
#                                                                                                'maxlength': 300,
#                                                                                                'placeholder': 'Insira aqui as instrucoes de pagamento e o valor do pedido para ser coletado pelo motoboy'
#                                                                                                }))
#
#
#
# class FormEditPonto(ModelForm, BaseForm):
#     telefone = forms.CharField(widget=forms.TextInput(attrs={'required': False, 'class': 'telefone',
#                                                              'maxlength': 200,
#                                                              'placeholder': 'Telefone do Cliente'}))
#     cliente = forms.CharField(widget=forms.TextInput(attrs={'required': False,
#                                                             'maxlength': 200,
#                                                             'placeholder': 'Nome do Cliente'}))
#
#     endereco = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'required': False,
#                                                                              'maxlength': 200,
#                                                                              'placeholder': 'Endereço'
#                                                                              }))
#     numero = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'required': False,
#                                                                          'maxlength': 200, 'class': 'numero',
#                                                                          'placeholder': 'Número'
#                                                                          }))
#     complemento = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'required': False,
#                                                                                 'maxlength': 200,
#                                                                                 'placeholder': 'Ponto de Referencia'
#                                                                                 }))
#     observacoes = forms.CharField(required=False, max_length=300, widget=forms.Textarea(attrs={'required': False,
#                                                                                                'maxlength': 300,
#                                                                                                'placeholder': 'Observações'
#                                                                                                }))
#
#     class Meta:
#         model = Ponto
#         fields = ['id', 'telefone', 'cliente', 'endereco', 'numero', 'bairro', 'complemento', 'observacoes']
#
#
# class FormRegister(ModelForm, BaseForm):
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True,
#                                                                'maxlength': 200,
#                                                                'placeholder': 'Nome Estabelecimento'}))
#     username = forms.CharField(widget=forms.TextInput(attrs={'required': True,
#                                                              'maxlength': 200,
#                                                              'placeholder': 'Login'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True,
#                                                                  'placeholder': 'Senha'}))
#     phone = forms.CharField(widget=forms.TextInput(attrs={'required': True,
#                                                           'maxlength': 200,
#                                                           'placeholder': 'Telefone'}))
#     endereco = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'required': True,
#                                                                             'maxlength': 200,
#                                                                             'placeholder': 'Endereço'
#                                                                             }))
#     numero = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'required': True,
#                                                                          'maxlength': 200,
#                                                                          'placeholder': 'Número'
#                                                                          }))
#     file = forms.FileField(required=False,
#                            widget=forms.FileInput(attrs={'required': True, 'placeholder': 'Logotipo do Estabelecimento'
#                                                          }))
#
#     class Meta:
#         model = Estabelecimento
#         fields = ['bairro', ]
#
#
# class FormEditPerfil(ModelForm, BaseForm):
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True,
#                                                                'maxlength': 200,
#                                                                'placeholder': 'Nome Estabelecimento'}))
#     phone = forms.CharField(widget=forms.TextInput(attrs={'required': True,
#                                                           'maxlength': 200,
#                                                           'placeholder': 'Telefone'}))
#     endereco = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'required': True,
#                                                                             'maxlength': 200,
#                                                                             'placeholder': 'Endereço'
#                                                                             }))
#     numero = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'required': True,
#                                                                          'maxlength': 200,
#                                                                          'placeholder': 'Número'
#                                                                          }))
#     file = forms.FileField(required=False,
#                            widget=forms.FileInput(attrs={'required': True, 'placeholder': 'Logotipo do Estabelecimento'
#                                                          }))
#
#     class Meta:
#         model = Estabelecimento
#         fields = ['bairro', ]
#
#
# class FormMotoristaRegister(ModelForm, BaseForm):
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True,
#                                                                'maxlength': 200,
#                                                                'placeholder': 'Nome Completo'}))
#     username = forms.CharField(widget=forms.TextInput(attrs={'required': True,
#                                                              'maxlength': 200,
#                                                              'placeholder': 'Login'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True,
#                                                                  'placeholder': 'Senha'}))
#     endereco = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'required': True,
#                                                                              'maxlength': 200,
#                                                                              'placeholder': 'Endereço'
#                                                                              }))
#     numero = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'required': True,
#                                                                          'maxlength': 200,
#                                                                          'placeholder': 'Número'
#                                                                          }))
#     phone = forms.CharField(widget=forms.TextInput(attrs={'required': True,
#                                                           'maxlength': 200,
#                                                           'placeholder': 'Telefone'}))
#     cpf = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'required': True,
#                                                                                        'maxlength': 200,
#                                                                                        'placeholder': 'CPF'
#                                                                                        }))
#     placa = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'required': True,
#                                                                                          'maxlength': 200,
#                                                                                          'placeholder': 'Placa do Veiculo'
#                                                                                          }))
#     file = forms.FileField(required=False,
#                            widget=forms.FileInput(attrs={'required': False, 'placeholder': 'Logotipo do Estabelecimento'
#                                                          }))
#
#     class Meta:
#         model = Motorista
#         fields = []
#
#
# PontoFormSet = inlineformset_factory(Pedido, Ponto, form=FormPonto, extra=1)
#
# PontoFormUpdateSet = inlineformset_factory(Pedido, Ponto, form=FormEditPonto, extra=0)
#
#
# class FormPontoCliente(ModelForm, BaseForm):
#     class Meta:
#         model = Ponto
#         fields = ['cliente', 'telefone', 'endereco', 'numero', 'bairro', 'complemento']
