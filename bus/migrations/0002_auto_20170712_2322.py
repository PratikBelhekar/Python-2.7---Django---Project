# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 04:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bustimetable',
            name='Ticket_cost',
        ),
        migrations.RemoveField(
            model_name='bustimetable',
            name='Total_Seats',
        ),
    ]
