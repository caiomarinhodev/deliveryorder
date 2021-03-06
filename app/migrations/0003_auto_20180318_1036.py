# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-18 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_estabelecimento_esta_aprovada'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='obrigatoriedade',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='troco',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='valor_total',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
