# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20171115_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='collection_point',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products_collect', to='product.ProductCollectionPoint', verbose_name='Local de coleta/colheita'),
        ),
    ]
