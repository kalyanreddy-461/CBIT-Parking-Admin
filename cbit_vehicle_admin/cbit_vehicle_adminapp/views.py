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

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    global token1
    url = 'https://cosc-vehicle.herokuapp.com/pending'
    approve = request.GET.get('approve')
    requests.put(url,headers = {'Authorization':'Bearer {}'.format(token1)},data={'reg_id' : approve})


    pending = requests.get(url,headers = {'Authorization':'Bearer {}'.format(token1)}).json()
    if len(pending)==0:
        messages.info(request,"No applications are available to approve!")
        return render(request,'cbit_vehicle_adminapp/register.html')
    else:
        context = {'pending' : pending}
        return render(request,'cbit_vehicle_adminapp/register.html',context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dismiss(request):
    global token1
    url = 'https://cosc-vehicle.herokuapp.com/dismiss'
    reg_id=request.GET.get('reg_id')

    requests.put(url,headers = {'Authorization':'Bearer {}'.format(token1)},data={'reg_id' : reg_id})
    messages.info(request,"successfully dismissed")
    return redirect('dismiss1')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dismiss2(request):
    global token1
    url = 'https://cosc-vehicle.herokuapp.com/dismiss'
    dismiss = requests.get(url,headers = {'Authorization':'Bearer {}'.format(token1)}).json()
    if len(dismiss)==0:
        messages.info(request,"No dismissed vehicles are available!")
        return redirect('listdismiss')
    else:
        context = {'dismiss' : dismiss}
        return render(request,'cbit_vehicle_adminapp/listdismiss.html',context)

def dismiss3(request):
    global token1
    url = 'https://cosc-vehicle.herokuapp.com/vechreg'
    reg_id=request.GET['reg_id']
    data=requests.get(url,headers = {'Authorization':'Bearer {}'.format(token1)},data={'reg_id' : reg_id})
    r=data.json()
    print(len(r))
    if (len(r)==0 or reg_id==''):
        messages.info(request,"invalid registration_id")
        return redirect('dismiss1')
    else:
        print(r)
        context={'details':r}
        return render(request,'cbit_vehicle_adminapp/dismiss.html',context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dismiss1(request):
    return render(request,'cbit_vehicle_adminapp/dismiss.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def listdismiss(request):
    return render(request,'cbit_vehicle_adminapp/listdismiss.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def fines(request):
    global token1
    pay = request.GET.get('pay')

    requests.put("https://cosc-vehicle.herokuapp.com/fine",headers = {'Authorization':'Bearer {}'.format(token1)},data={'request_id' : pay})


    data = requests.get("https://cosc-vehicle.herokuapp.com/fine",
								headers = {'Authorization':'Bearer {}'.format(token1)})
    payment1=[]
    r=data.json()
    print(r)
    if len(r)==0:
        messages.info(request,"No fine payments available!")
        return render(request,'cbit_vehicle_adminapp/fines.html')

    else:
        for i in range(0,len(r)):
            payment_details1={
                'user_id':r[i]['user_id'],
                'fine': r[i]['fine'],
                'type_of_request': r[i]['type_of_request'],
                'payment_date': r[i]['payment_date'][0:16],
                'request_id':r[i]['request_id'],
                'Registration_id':r[i]['reg_id']
                }
            payment1.append(payment_details1)
        context = {'payment1':payment1}
        return render(request,'cbit_vehicle_adminapp/fines.html',context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def fine(request):
    return render(request,'cbit_vehicle_adminapp/fines.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def paystatistic(request):
    return render(request,'cbit_vehicle_adminapp/paystatistics.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def regstatistic(request):
    return render(request,'cbit_vehicle_adminapp/regstatistics.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def paystatistics(request):
    global token1
    date=request.GET['date']
    date1="".join(date.split('-'))
    print(date1)

    data = requests.get("https://cosc-vehicle.herokuapp.com/paymentstats",
								headers = {'Authorization':'Bearer {}'.format(token1)},
								data = {"payment_date":date1})
    payment=[]
    r=data.json()
    print(r)
    if len(r)==0:
        messages.info(request,"No payments are available on selected date!")
        return redirect('paystatistic')
    for i in r:
        if 'message' in i:
            messages.info(request,"please select the date")
            return redirect('paystatistic')
        else:
            for i in range(0,len(r)):
                payment_details={
                'user_id':r[i]['user_id'],
                'fine': r[i]['fine'],
                'date':date,
                'type_of_request': r[i]['type_of_request'],
                'request_id':r[i]['request_id'],
                'Registration_id':r[i]['reg_id'],
                'payment_status':r[i]['payment_status']
            }
                payment.append(payment_details)
            context = {'payment':payment}
            return render(request,'cbit_vehicle_adminapp/paystatistics.html',context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def regstatistics(request):
    global token1
    date=request.GET['date']
    date1="".join(date.split('-'))
    print(date1)

    data = requests.get("https://cosc-vehicle.herokuapp.com/regstats",
								headers = {'Authorization':'Bearer {}'.format(token1)},
								data = {"updated_date":date1})
    payment=[]
    r=data.json()
    if len(r)==0:
        messages.info(request,"No registrations are available on selected date!")
        return redirect('regstatistic')
    for i in r:
        if 'message' in i:
            messages.info(request,"please select the date")
            return redirect('regstatistic')
        else:
            context = {'r':r}
            return render(request,'cbit_vehicle_adminapp/regstatistics.html',context)
