# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-16 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180313_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='descricao',
            field=models.TextField(default=''),
        ),
    ]
