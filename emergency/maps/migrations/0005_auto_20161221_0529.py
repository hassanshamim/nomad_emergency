# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 05:29
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0004_auto_20161218_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]