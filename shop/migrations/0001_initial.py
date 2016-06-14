# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 17:12
from __future__ import unicode_literals

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='Заголовок')),
                ('description', ckeditor.fields.RichTextField(default='', verbose_name='Описание')),
                ('pub_date', models.DateField(default=datetime.datetime(2016, 6, 1, 17, 12, 39, 352148, tzinfo=utc), verbose_name='Дата публикации')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='NewsImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.News', verbose_name='Новость')),
            ],
            options={
                'ordering': ['-key'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=100, verbose_name='ФИО')),
                ('address', models.CharField(default='', max_length=200, verbose_name='Адрес')),
                ('tel_number', models.IntegerField(default=0, verbose_name='Номер телефона')),
                ('product_name', models.CharField(default='', max_length=200, verbose_name='Название товара')),
                ('price', models.IntegerField(default=0, verbose_name='Цена товара')),
                ('order_date', models.DateTimeField(default=datetime.datetime(2016, 6, 1, 17, 12, 39, 354153, tzinfo=utc), verbose_name='Дата заказа')),
            ],
            options={
                'ordering': ['-order_date'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=200, verbose_name='Название товара')),
                ('price', models.IntegerField(default=0, verbose_name='Цена товара')),
                ('description', ckeditor.fields.RichTextField(max_length=5000, verbose_name='Описание товара')),
                ('in_stock', models.BooleanField(default=False, verbose_name='В наличии')),
                ('in_kit', models.TextField(blank=True, default='', max_length=5000, null=True, verbose_name='В наборе')),
                ('save_date', models.DateTimeField(default=datetime.datetime(2016, 6, 1, 17, 12, 39, 355150, tzinfo=utc), verbose_name='Дата добавления')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='my_cms.ProductGroup', verbose_name='Группа товара')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='my_cms.ManufacturerList', verbose_name='Производитель')),
            ],
            options={
                'ordering': ['-save_date'],
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Фотография товара')),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.Product', verbose_name='Товар')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Имя')),
                ('tel_number', models.IntegerField(default=0, verbose_name='Номер телефона')),
                ('time', models.CharField(default='', max_length=50, verbose_name='Время')),
                ('date', models.CharField(default='', max_length=50, verbose_name='Дата')),
                ('save_date', models.DateField(default=datetime.datetime(2016, 6, 1, 17, 12, 39, 354153, tzinfo=utc), verbose_name='Дата сохранения')),
            ],
            options={
                'ordering': ['-save_date'],
            },
        ),
    ]
