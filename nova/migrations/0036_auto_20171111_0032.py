# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-10 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0035_auto_20171111_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesskey',
            name='access_sec',
            field=models.CharField(max_length=200, verbose_name='Access Secret'),
        ),
    ]