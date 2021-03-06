# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-10 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VolcanesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volcanes',
            name='LATITUD_DECIMALES',
            field=models.DecimalField(decimal_places=20, default=0, max_digits=23),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volcanes',
            name='LONGITUD_DECIMALES',
            field=models.DecimalField(decimal_places=20, default=0, max_digits=23),
            preserve_default=False,
        ),
    ]
