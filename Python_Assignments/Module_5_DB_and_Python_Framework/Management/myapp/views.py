from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductSubCategory
from .forms import ProductForm, ProductSubCategoryForm

def home(request):
    return render(request, 'home.html')

def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')

def product_manager_dashboard(request):
    return render(request, 'product_manager/product_manager_dashboard.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm()
    return render(request, 'admin/add_product.html', {'form': form})

def add_product_sub_category(request):
    if request.method == 'POST':
        form = ProductSubCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductSubCategoryForm()
    return render(request, 'admin/add_product_sub_category.html', {'form': form})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'admin/edit_product.html', {'form': form})

def search_product(request):
    query = request.GET.get('query')
    products = Product.objects.filter(name__icontains=query)
    return render(request, 'product_manager/search_results.html', {'products': products})
