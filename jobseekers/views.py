from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'jobseekers/login.html')

def search(request):
    return render(request,'jobseekers/jobsearch.html')

def deatail(request):
    return render(request,'jobseekers/jobdeatails.html')

