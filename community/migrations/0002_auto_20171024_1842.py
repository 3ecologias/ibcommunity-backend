# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 21:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='communities', to='product.Product', verbose_name='Produtos'),
        ),
        migrations.AlterField(
            model_name='communityleadership',
            name='phone',
            field=models.CharField(max_length=255, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='communityleadership',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.CommunityLeadershipType', verbose_name='Tipo de liderança'),
        ),
    ]
