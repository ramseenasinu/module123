from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'emplooyes/login.html')

def home(request):
    return render(request,'home/home.html')