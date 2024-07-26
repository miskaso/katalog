from django.urls import path, include
from . import views
from .views import *



urlpatterns = [
    path('', product_list, name='home'),
    path('<int:pk>', views.DetailProduct.as_view(), name='detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]
