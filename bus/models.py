# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.db import models

# Create your models here.

class BusTimeTable(models.Model):
    Bus_name = models.CharField(max_length = 200)
    bus_license_plate = models.CharField( max_length = 20)
    Depart_Date = models.DateField( max_length = 10)
    Depart_Time = models.CharField( max_length = 10)
    Depart_Location = models.CharField( max_length = 50)
    Arrival_Date = models.DateField(max_length=10)
    Arrival_Time = models.CharField(max_length=10)
    Arrival_Location = models.CharField(max_length=50)
    Total_Seats = models.CharField(max_length=50,default=None)
    Ticket_cost = models.CharField(max_length=50, default=None)

class Registration(models.Model):
    user = models.ForeignKey(User, default=1)
    bus = models.ForeignKey(BusTimeTable, on_delete=models.CASCADE)
    seats_booked = models.CharField(max_length=50)
    cost = models.CharField(max_length=50, default=None)







