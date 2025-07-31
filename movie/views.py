from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to home page</h1")

def about(request):
    return HttpResponse("<h1>About us</h1><p>This is the about page of our movie review site.</p>")

def home(request):
    # return HttpResponse('<h1>Welcome to home page</h1>')
    # return render(request, 'home.html')
    return render(request, 'home.html', {'name': 'Samu Arango'})