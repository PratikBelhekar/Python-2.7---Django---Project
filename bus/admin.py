# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import BusTimeTable, Registration
# Register your models here.

admin.site.register(BusTimeTable)
admin.site.register(Registration)