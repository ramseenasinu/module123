from django.shortcuts import render

# Create your views here.

def homes(request):
    return render(request,'jadm/home.html')

def loges(request):
    return render(request,'jadm/login.html')
