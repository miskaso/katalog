from django.shortcuts import render, redirect
from .models import Product

def product_list(request):
    category = request.GET.get('category')
    products = Product.object.all()
    if category:
        products = products.filter(category=category)
    return render(request, 'product_list.html', {'products': products})





# class ProductView(ListView):
#     template_name = 'index.html'
#     model = Product
#     context_object_name = 'products'
#     paginate_by = 10
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get