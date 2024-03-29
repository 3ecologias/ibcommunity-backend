# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyDemography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('man_number', models.PositiveIntegerField(default=0, help_text='Quantidade de homens entre 18-65 anos da família', verbose_name='Número de homens')),
                ('woman_number', models.PositiveIntegerField(default=0, help_text='Quantidade de mulheres entre 18-65 anos da família', verbose_name='Número de mulheres')),
                ('young_man_number', models.PositiveIntegerField(default=0, help_text='Quantidade de homens entre 12-24 anos da família', verbose_name='Número de homens jovens')),
                ('young_woman_number', models.PositiveIntegerField(default=0, help_text='Quantidade de mulheres entre 12-24 anos da família', verbose_name='Número de mulheres jovens')),
                ('kids_number', models.PositiveIntegerField(default=0, help_text='Quantidade de crianças da família', verbose_name='Número de crianças')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('family', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='family.Family', verbose_name='Família relacionada')),
            ],
            options={
                'verbose_name': 'Demografia Famílias',
                'verbose_name_plural': 'Demografia das Famílias',
                'ordering': ['-created_at'],
            },
        ),
    ]
