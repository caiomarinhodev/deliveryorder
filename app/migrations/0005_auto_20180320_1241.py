# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-20 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_pedido_endereco_entrega'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfiguracaoSistema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('is_feriado', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bairro',
            name='valor',
            field=models.CharField(default='6', max_length=3),
        ),
        migrations.AddField(
            model_name='bairro',
            name='valor_feriado',
            field=models.CharField(default='9', max_length=3),
        ),
        migrations.AddField(
            model_name='bairro',
            name='valor_madrugada',
            field=models.CharField(default='8', max_length=3),
        ),
        migrations.AddField(
            model_name='bairro',
            name='valor_madrugada_feriado',
            field=models.CharField(default='11', max_length=3),
        ),
        migrations.AddField(
            model_name='endereco',
            name='valor_entrega',
            field=models.CharField(blank=True, default='6', max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='subtotal',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
