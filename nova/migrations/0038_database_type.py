# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-22 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0037_uploadfile_file_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='type',
            field=models.CharField(default='mysql', max_length=20, verbose_name='\u6570\u636e\u5e93\u7c7b\u578b'),
            preserve_default=False,
        ),
    ]