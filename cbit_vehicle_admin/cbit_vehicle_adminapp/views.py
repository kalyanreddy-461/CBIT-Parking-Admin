from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def register(request):
    return render(request,'index.html')

def dismiss(request):
    return render(request,'dismiss.html')

def fines(request):
    return render(request,'fines.html')

def statistics(request):
    return render(request,'statistics.html')
