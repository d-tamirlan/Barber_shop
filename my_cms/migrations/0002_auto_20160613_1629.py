# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='info',
            field=models.TextField(default='', max_length=5000, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='working_time',
            field=models.TextField(default='', max_length=1000, verbose_name='Время работы'),
        ),
    ]