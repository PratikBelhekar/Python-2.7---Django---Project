# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0005_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='cost',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
