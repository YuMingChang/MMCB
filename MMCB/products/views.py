from django.shortcuts import render#, get_object_or_404
from .models import Product

# Create your views here.
def store_list(request):
    QuerySet = Product.objects.all()
    context = {
        'title' : 'MMCB_StoreList',
        'Product_ObjList': QuerySet
    }
    return render(request, 'products/store_list.html', context)
