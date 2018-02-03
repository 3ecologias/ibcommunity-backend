# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scientific_name', models.CharField(max_length=255, verbose_name='Nome científico')),
                ('common_name', models.CharField(max_length=255, verbose_name='Nome popular')),
                ('provenance', models.CharField(choices=[('natural', 'Natural'), ('plantio', 'Plantio'), ('saf', 'SAF')], max_length=255, verbose_name='Procedência')),
                ('is_threatened', models.BooleanField(verbose_name='Espécie ameaçada?')),
                ('fruit_anual_volume', models.PositiveIntegerField(default=0, help_text='Em KG', verbose_name='Voume anual do fruto')),
                ('seed_anual_volume', models.PositiveIntegerField(default=0, help_text='Em KG', verbose_name='Voume anual da semente')),
                ('pulp_anual_volume', models.PositiveIntegerField(default=0, help_text='Em KG', verbose_name='Voume anual da polpa')),
                ('harvest_period', models.TextField(blank=True, help_text='Informações sobre o período da safra', null=True, verbose_name='Período da safra')),
                ('certification_origin', models.TextField(blank=True, help_text='Informações sobre o orgão que expediu                                                        a certificação do produto.', verbose_name='Orgão da certificação')),
                ('benefit_sharing_value', models.TextField(verbose_name='Regra de repartição de benefício')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProductCollectionPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_type', models.CharField(choices=[('area_propria', 'Área própria'), ('area_compartilhada', 'Área compartilhada'), ('area_cedida', 'Área cedida'), ('praia', 'Praia'), ('rio', 'Rio')], max_length=255, verbose_name='Local da coleta/colheita')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Local de coleta/colheita',
                'verbose_name_plural': 'Locais de coleta/colheita',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='collection_point',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='products_collect', to='product.ProductCollectionPoint', verbose_name='Local de coleta/colheita'),
        ),
    ]