from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def index(request):
    return render(request, 'accounts/index.html')