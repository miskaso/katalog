from django.shortcuts import render, redirect
from .models import Product

def product_list(request):
    category = request.GET.get('category')
    products = Product.object.all()
    if category:
        products = products.filter(category=category)
    return render(request, 'product_list.html', {'products': products})

