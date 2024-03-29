# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 23:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='benefit_sharing_value',
            field=models.TextField(null=True, verbose_name='Regra de repartição de benefício'),
        ),
        migrations.AlterField(
            model_name='product',
            name='certification_origin',
            field=models.TextField(blank=True, help_text='Informações sobre o orgão que expediu                                                        a certificação do produto.', null=True, verbose_name='Orgão da certificação'),
        ),
        migrations.AlterField(
            model_name='product',
            name='collection_point',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products_collect', to='product.ProductCollectionPoint', verbose_name='Local de coleta/colheita'),
        ),
        migrations.AlterField(
            model_name='product',
            name='provenance',
            field=models.CharField(blank=True, choices=[('desconhecida', 'Desconhecida'), ('natural', 'Natural'), ('plantio', 'Plantio'), ('saf', 'SAF')], max_length=255, null=True, verbose_name='Procedência'),
        ),
        migrations.AlterField(
            model_name='product',
            name='scientific_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome científico'),
        ),
    ]
