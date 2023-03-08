from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sample(request):
    return HttpResponse("<marquee><h1>HI</h1></marquee>")

def sample1(repuest):
    return HttpResponse("<h1>this is my website</h1>")