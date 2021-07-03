from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'website/index.html')

def paraPartial(request):
    return render(request, 'website/para.html')