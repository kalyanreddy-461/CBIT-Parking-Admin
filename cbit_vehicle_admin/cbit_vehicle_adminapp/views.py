from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def register(request):
    return render(request,'cbit_vehicle_adminapp/register.html')

def dismiss(request):
    return render(request,'cbit_vehicle_adminapp/dismiss.html')

def fines(request):
    return render(request,'cbit_vehicle_adminapp/fines.html')

def statistics(request):
    return render(request,'cbit_vehicle_adminapp/statistics.html')
