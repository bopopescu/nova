# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-12-05 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0044_auto_20171201_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='detail',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='\u4efb\u52a1\u8be6\u60c5'),
        ),
    ]