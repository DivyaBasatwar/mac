from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def features(request):
    return render(request,"features.html")

def pricing(request):
    return render(request,"pricing.html")

def feedback(request):
    return render(request,"feedback.html")
