from django.shortcuts import render
from products.models import Product

def store_list(request):
    QuerySet = Product.objects.all()
    context = {
        'title' : 'MMCB_StoreList',
        'Product_ObjList': QuerySet
    }
    return render(request, 'products/store_list.html', context)
