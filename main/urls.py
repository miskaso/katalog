from django.urls import path, include
from views import product_list
from . import views
urlpatterns = [
    path('', product_list, name='product_list'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]
