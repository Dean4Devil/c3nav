# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessoperator',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
    ]
