# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render
from .models import BusTimeTable,Registration
from forms import UserForm
from reportlab.pdfgen import canvas


def index(request):
    bus = BusTimeTable.objects.all()
    for busl in bus:
        location = bus.values('Depart_Location').distinct()
        arrival = bus.values('Arrival_Location').distinct()
        context = {'location': location, 'arrival': arrival, }
    return render(request,'bus/index.html',context)

def lindex(request):
    bus = BusTimeTable.objects.all()
    for busl in bus:
        location = bus.values('Depart_Location').distinct()
        arrival = bus.values('Arrival_Location').distinct()
        context = {'location': location, 'arrival': arrival, }
    print context,"/*******"
    return render(request,'bus/lindex.html',context)

def searchResult(request):
    searchbus = BusTimeTable.objects.all()
    bus = BusTimeTable.objects.all()
    for busl in bus:
        location = bus.values('Depart_Location').distinct()
        arrival = bus.values('Arrival_Location').distinct()

    sdepart = request.POST['departure']
    sarrival = request.POST['arrival']

    if sdepart != sarrival :
        msg = "ok"
        #scontext = {'sbus':BusTimeTable.objects.filter(Depart_Location = sdepart,Arrival_Location = sarrival ),'msg':msg}
    else:
        msg = "Not ok"
    # return render(request, 'bus/index.html', scontext)
    return render(request, 'bus/index.html', {'location': location, 'arrival': arrival,'sbus':BusTimeTable.objects.filter(Depart_Location = sdepart,Arrival_Location = sarrival ),'msg':msg})

def lsearchResult(request):
    searchbus = BusTimeTable.objects.all()
    bus = BusTimeTable.objects.all()
    for busl in bus:
        location = bus.values('Depart_Location').distinct()
        arrival = bus.values('Arrival_Location').distinct()

    sdepart = request.POST['departure']
    sarrival = request.POST['arrival']

    if sdepart != sarrival :
        msg = "ok"
        #scontext = {'sbus':BusTimeTable.objects.filter(Depart_Location = sdepart,Arrival_Location = sarrival ),'msg':msg}
    else:
        msg = "Not ok"
    # return render(request, 'bus/index.html', scontext)
    return render(request, 'bus/lindex.html', {'location': location, 'arrival': arrival,'sbus':BusTimeTable.objects.filter(Depart_Location = sdepart,Arrival_Location = sarrival ),'msg':msg})


def register(request):
    bus = BusTimeTable.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            for busl in bus:
                location = bus.values('Depart_Location').distinct()
                arrival = bus.values('Arrival_Location').distinct()
                context = {'location': location, 'arrival': arrival, }
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user.set_password(raw_password)
            user.save()
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request,'bus/lindex.html',context)
    form = UserForm()
    return render(request, 'bus/register.html', {'form': form})

def login_user(request):
    bus = BusTimeTable.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                for busl in bus:
                    location = bus.values('Depart_Location').distinct()
                    arrival = bus.values('Arrival_Location').distinct()

                    context = {'location': location, 'arrival': arrival, 'username':username}

                return render(request, 'bus/lindex.html', context)
            else:
                return render(request, 'bus/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'bus/login.html', {'error_message': 'Invalid login'})
    return render(request, 'bus/login.html')


def logout(request):
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'bus/login.html', context)

def book(request):
    #bus = BusTimeTable.objects.all()

    busid = request.POST['bus']
    selectedbus = BusTimeTable.objects.filter(pk =busid)


    context = {'busid':busid,'selectedbus':selectedbus,}
    return render (request,'bus/bookingform.html',context)

def confirm(request):

    bus = BusTimeTable.objects.all()

    totalseats = int(request.POST['bseats'])
    busid = request.POST['bid']
    selbus = BusTimeTable.objects.filter(pk =busid)
    for selbus in selbus:
        Total_Seat = int(selbus.Total_Seats)
        Total_Sea = Total_Seat - totalseats
        selbus.Total_Seats = str(Total_Sea)
        cost = selbus.Ticket_cost
    selbus.save()
    cost = cost.split("$")
    cost = int(cost[1]) * totalseats

    #update registaration table
    current_user = request.user
    print current_user,"***********"

    Registration.objects.create(user = current_user, bus = selbus, seats_booked=str(totalseats), cost=str(cost))

    registration = Registration.objects.all()
    context = {"selbus":selbus,"registration":registration,"totalseats":totalseats,"cost":cost}
    return render(request,'bus/viewbooking.html',context)


def bookingHistory(request):
    #bus = BusTimeTable.objects.all()
    c_user = request.user
    #print c_user,"=="
    busid=[]
    msg = "No Record Found"
    for reg in Registration.objects.select_related().filter(user=c_user):
        if reg is not None:
            #print "hello"
            #print reg.pk,"-----------------"
            msg = "yes"
            busid = reg.bus.id
            cost = reg.cost
            seats= reg.seats_booked
            context = {"cost":cost, "seats":seats}


    if msg=="yes":
        context={"pk":reg.pk,"msg":msg,"bbus":BusTimeTable.objects.filter(pk=busid),"cost":cost, "seats":seats}
        return render(request, 'bus/bookingHistory.html', context)
    else:
        return render(request,'bus/bookingHistory.html',{"msg":msg})

def cancel(request):
    reserid = request.POST['rid']

    Registration.objects.filter(pk=reserid).delete()
    c_user = request.user
    # print c_user,"=="
    busid = []
    msg = "Selected Record is Deleted"
    for reg in Registration.objects.select_related().filter(user=c_user):
        if reg is not None:
            # print "hello"
            # print reg.pk,"-----------------"
            msg = "yes"
            busid = reg.bus.id
            cost = reg.cost
            seats = reg.seats_booked
            context = {"cost": cost, "seats": seats}

    if msg == "yes":
        context = {"pk": reg.pk, "msg": msg, "bbus": BusTimeTable.objects.filter(pk=busid), "cost": cost,
                   "seats": seats}
        return render(request, 'bus/bookingHistory.html', context)
    else:
        return render(request, 'bus/bookingHistory.html', {"msg": msg})
