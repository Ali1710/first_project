from django.shortcuts import render
from models11 import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})
