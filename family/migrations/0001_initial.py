# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=255, verbose_name='Nome da família')),
                ('interviewee_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome do entrevistado')),
                ('leader_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome do líder da família')),
                ('leader_sex', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=255, null=True, verbose_name='Sexo do líder da família')),
                ('leader_phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefone do líder da família')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email para contato')),
                ('occupation', models.TextField(blank=True, help_text='Descrição da ocupação atual do representante da família', null=True, verbose_name='Ocupação')),
                ('images_license', models.FileField(blank=True, null=True, upload_to='family/licenses/image/%m/%y', verbose_name='Licença de autorização de uso da imagem')),
                ('future_vision', models.TextField(blank=True, help_text='Descrição da visão de futuro da família', null=True, verbose_name='Visão de futuro')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Família (dados gerais)',
                'verbose_name_plural': 'Famílias (dados gerais)',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='FamilyHealthProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_problem', models.CharField(max_length=255, verbose_name='Tipo do problema de saúde')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Problema de saúde',
                'verbose_name_plural': 'Problemas de saúde',
            },
        ),
        migrations.CreateModel(
            name='FamilyPictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome da imagem')),
                ('image', models.ImageField(upload_to='family/pictures/%y/%m', verbose_name='Imagem')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='family.Family', verbose_name='Família')),
            ],
            options={
                'verbose_name': 'Imagem da família',
                'verbose_name_plural': 'Imagens das famílias',
                'ordering': ['-uploaded_at'],
            },
        ),
        migrations.CreateModel(
            name='FamilySources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_type', models.CharField(max_length=255, verbose_name='Tipo de fonte de renda')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Fonte de renda',
                'verbose_name_plural': 'Fontes de renda',
            },
        ),
        migrations.AddField(
            model_name='family',
            name='health_problems',
            field=models.ManyToManyField(help_text='Descrição das doenças crônicas e sobre condições de saúde da família ', to='family.FamilyHealthProblem', verbose_name='Problemas de saúde'),
        ),
        migrations.AddField(
            model_name='family',
            name='incoming_sources',
            field=models.ForeignKey(help_text='Descrição da principal fonte de renda do representante da família', on_delete=django.db.models.deletion.CASCADE, to='family.FamilySources', verbose_name='Fontes de renda'),
        ),
    ]
