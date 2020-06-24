from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.db import models
import requests
global token1
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def base(request):
    return render (request,"cbit_vehicle_adminapp/base.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.method=='POST':
        global token1
        adminid=request.POST['adminid']
        password=request.POST['password']
        token=requests.post(' https://cosc-vehicle.herokuapp.com/login',data={'user_id':adminid,'password':password,'usertype':'admin'})
        print(token.json())
        for i in token.json():
            if 'message' in i:
                messages.info(request,"invalid credentials")
                return redirect('login')
            else:
                token1=token.json()['access_token']
                return redirect('register')

    else:
        return render(request,"cbit_vehicle_adminapp/login.html")

def register(request):
    return render(request,'cbit_vehicle_adminapp/register.html')

def dismiss(request):
    return render(request,'cbit_vehicle_adminapp/dismiss.html')

def fines(request):
    global token1
    date=request.GET['date']
    date1="".join(date.split('-'))
    print(date1)
    url='https://cosc-vehicle.herokuapp.com/fine'
    data = requests.get("https://cosc-vehicle.herokuapp.com/fine",
								headers = {'Authorization':'Bearer {}'.format(token1)},
								data = {"payment_date":date1})
    payment=[]
    r=data.json()
    print(r)
    for i in range(0,len(r)):
        payment_details={
            'user_id':r[i]['user_id'],
            'fine': r[i]['fine'],
            'date':date
            }
        payment.append(payment_details)

    print(payment)
    context = {'payment':payment}
    return render(request,'cbit_vehicle_adminapp/fines.html',context)

def fine(request):
    return render(request,'cbit_vehicle_adminapp/fines.html')


def regstatistics(request):
    return render(request,'cbit_vehicle_adminapp/regstatistics.html')

def paystatistics(request):
    return render(request,'cbit_vehicle_adminapp/paystatistics.html')
