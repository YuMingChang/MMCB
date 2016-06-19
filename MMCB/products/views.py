from django.shortcuts import render
from .models import Product

# Create your views here.
def store_list(request):
    AllProduct = Product.objects.all()
    return render(request, 'products/store_list.html', {'AllProduct': AllProduct})


def product_add(request):
    return render(request, 'products/product_add.html')

def product_edit(request):
    return render(request, 'products/product_edit.html')

def product_delete(request):
    return render(request, 'products/product_delete.html')
