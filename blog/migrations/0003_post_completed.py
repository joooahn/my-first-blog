# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-03 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181103_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]