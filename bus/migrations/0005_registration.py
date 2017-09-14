# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 20:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bus', '0004_auto_20170719_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats_booked', models.CharField(max_length=50)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.BusTimeTable')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
