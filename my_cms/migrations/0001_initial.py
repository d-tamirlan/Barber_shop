# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 17:12
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description1', ckeditor.fields.RichTextField(default='', max_length=5000, verbose_name='Превое описание')),
                ('description2', ckeditor.fields.RichTextField(default='', max_length=5000, verbose_name='Второе описание')),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', ckeditor.fields.RichTextField(default='', max_length=5000, verbose_name='Информация')),
                ('working_time', ckeditor.fields.RichTextField(default='', max_length=1000, verbose_name='Время работы')),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Заголовок')),
                ('description', ckeditor.fields.RichTextField(default='', max_length=5000, verbose_name='Описание')),
                ('number', models.IntegerField(default=0, verbose_name='Номер в очереди')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='ManufacturerList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Название')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nav_item', models.CharField(default='', max_length=100, verbose_name='Элемент навигации')),
                ('url', models.CharField(default='/писать между слешами/', max_length=100, verbose_name='Ссылка')),
                ('number', models.IntegerField(default=0, verbose_name='Номер в очереди')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(default='', max_length=100, verbose_name='Услуга')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Название')),
            ],
        ),
    ]
