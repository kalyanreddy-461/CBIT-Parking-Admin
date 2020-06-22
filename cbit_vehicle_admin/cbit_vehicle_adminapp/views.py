from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.db import models
import requests

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def base(request):
    return render (request,"cbit_vehicle_adminapp/base.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.method=='POST':
        adminid=request.POST['adminid']
        password=request.POST['password']
        x1="cbit123123"
        y1="cbit123123"
        if adminid==x1 and password ==y1:
            return redirect('register')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
        return render(request,"cbit_vehicle_adminapp/login.html")

def register(request):
    return render(request,'cbit_vehicle_adminapp/register.html')

def dismiss(request):
    return render(request,'cbit_vehicle_adminapp/dismiss.html')

def fines(request):
    return render(request,'cbit_vehicle_adminapp/fines.html')

def regstatistics(request):
    return render(request,'cbit_vehicle_adminapp/regstatistics.html')

def paystatistics(request):
    return render(request,'cbit_vehicle_adminapp/paystatistics.html')
