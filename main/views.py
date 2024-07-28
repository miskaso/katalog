from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ProductForm
from django.views.generic import DetailView


from django.shortcuts import render
from .models import Product

@login_required
def product_list(request):
    selected_category = request.GET.get('category')
    products = Product.objects.all()
    if selected_category:
        products = products.filter(category=selected_category)
    categories = Product.objects.values_list('category', flat=True).distinct()
    return render(request, 'product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category
    })



def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'home.html', {'Ошибка': 'Неверный логин или пароль'})
    return render(request, 'home.html')


# class ProductView(ListView):
#     template_name = 'index.html'
#     model = Product
#     context_object_name = 'products'
#     paginate_by = 10
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get


# class DetailProduct(DetailView):
#     template_name = 'detail.html'
#     model = Product
#     context_object_name = 'detail'
#     slug_field = 'slug'

@login_required
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_detail.html', {'product': product})


def home(request):
    return render(request, 'home.html')
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../product_list')
    else:
        form = Product()
    return render(request, 'add_product.html', {'form': form})