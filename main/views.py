from django.shortcuts import render
from .models import Product
from django.views.generic import ListView

# Create your views here.


def index(req):
    return render(req, "index.html")


# class ProductView(ListView):
#     template_name = 'index.html'
#     model = Product
#     context_object_name = 'products'
#     paginate_by = 10
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get