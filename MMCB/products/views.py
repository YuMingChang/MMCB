from django.shortcuts import render
from products.models import Product


def store_list(request):
    all_products = Product.objects.all()
    context = {
        'title': 'StoreList',
        'All_Products': all_products
    }
    return render(request, 'products/store_list.html', context)
