from django.http import HttpResponse
from django.shortcuts import render

from carton.cart import Cart
# from products.models import Product
from products.models import Detail


def add(request):
    cart = Cart(request.session)
    product = Detail.objects.get(id=request.GET.get('id'))
    quantity = request.GET.get('quantity');
    cart.add(product, quantity, price=product.price)
    return HttpResponse("Added")


def remove(request):
    cart = Cart(request.session)
    product = Detail.objects.get(id=request.GET.get('id'))
    cart.remove(product)
    return HttpResponse("Removed")


def show(request):
    return render(request, 'shopping/show-cart.html')
