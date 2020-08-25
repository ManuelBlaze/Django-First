from django.http import HttpResponse
from django.template import Template
from django.shortcuts import render

#First View
def home(request):
    return render(request, 'index.html')

#Second View
# def greeting(request):
#     return HttpResponse('<h1>Welcome to the Django course with Python!</h1>')