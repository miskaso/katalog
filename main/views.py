from django.shortcuts import render, redirect
from .models import Product
from django.views.generic import DetailView

# Create your views here.


def product_list(request):
    category = request.GET.get('category')
    products = Product.objects.all()
    if category:
        products = products.filter(category=category)
    return render(request, 'product_list.html', {'products': products})


class DetailProduct(DetailView):
    template_name = 'detail.html'
    model = Product
    context_object_name = 'detail'
    slug_field = 'slug'
