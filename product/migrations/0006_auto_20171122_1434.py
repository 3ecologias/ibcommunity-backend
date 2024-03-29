# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20171122_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='harvest_period',
            field=models.ManyToManyField(blank=True, help_text='Informações sobre o período da safra', to='product.ProductHarvestPeriod', verbose_name='Período da safra'),
        ),
        migrations.AlterField(
            model_name='productharvestperiod',
            name='harvest_period',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=255, unique=True, verbose_name='Período'),
        ),
    ]
