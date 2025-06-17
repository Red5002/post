# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('hello world, welcome to the home page')
    return render(request, 'home.html')

def aboutpage(request):
    # return HttpResponse('welcome to the about page')
    return render(request, 'about.html')