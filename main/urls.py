from django.urls import path, include
from . import views
from .views import *



urlpatterns = [
    path('', home, name='home'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('product_list/', product_list, name='product_list'),
    path('register/', views.register_view, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_product/', views.add_product, name='add_product'),

]
