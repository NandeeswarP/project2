from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sample(request):
    return HttpResponse("<strong>hi hello</strong>")

def sample1(request):
    return HttpResponse("<marquee>GOD</marquee>")