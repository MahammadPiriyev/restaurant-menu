from datetime import date
from django.shortcuts import render
from .models import Menu, Category

def home(request):
    products = Menu.objects.all()
    categories = Category.objects.all()
    context = {
        "categories":categories,
        "products":products
    }

    return render(request, 'index.html', context)

def category_detail(request, category_slug):
    products = Menu.objects.all().filter(category__slug=category_slug)
    categories = Category.objects.all()
    context = {
        'products':products,
        'categories':categories
    }
    return render(request, "index.html",context)