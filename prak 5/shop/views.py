from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'shop/index.html')

def basket(request):
    return render(request, 'shop/basket.html')

def pg3(request):
    return render(request, 'shop/pg3.html')

def pg4(request):
    return render(request, 'shop/pg4.html')

def pg5(request):
    return render(request, 'shop/pg5.html')