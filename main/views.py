from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
@login_required
def product_list(request):
    category = request.GET.get('category')
    products = Product.object.all()
    if category:
        products = products.filter(category=category)
    return render(request, 'product_list.html', {'products': products})


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guestbook')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('guestbook')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


# class ProductView(ListView):
#     template_name = 'index.html'
#     model = Product
#     context_object_name = 'products'
#     paginate_by = 10
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get