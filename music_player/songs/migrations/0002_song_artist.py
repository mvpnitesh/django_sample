# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
