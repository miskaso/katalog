from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('', product_list, name='home'),
    path('<int:pk>', views.DetailProduct.as_view(), name='detail')
]
