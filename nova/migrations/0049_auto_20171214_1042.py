# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-12-14 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0048_httpstep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='httpstep',
            name='timeout',
            field=models.CharField(default=15, max_length=20, verbose_name='\u8d85\u65f6\u65f6\u95f4'),
        ),
    ]