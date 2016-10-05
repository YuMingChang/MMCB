from django.urls import reverse
from django.shortcuts import render, redirect

from carton.cart import Cart
from products.models import Detail


def add(request):
    cart = Cart(request.session)
    product = Detail.objects.get(id=request.GET.get('id'))
    quantity = request.GET.get('quantity')
    cart.add(product, quantity, price=product.price)
    return redirect(reverse('store'))


def remove(request):
    cart = Cart(request.session)
    product = Detail.objects.get(id=request.GET.get('id'))
    cart.remove(product)
    return redirect(reverse('cart:shopping-cart-show'))


def clear(request):
    cart = Cart(request.session)
    cart.clear()
    return redirect(reverse('cart:shopping-cart-show'))


def show(request):
    if request.method == 'POST':
        cart = Cart(request.session)
        try:
            quantityList = request.POST.getlist('quantity')
            for idx, item in enumerate(cart.products):
                cart.set_quantity(item, quantityList[idx])
            return redirect(reverse('checkout:page'))
        except:
            pass
    return render(request, 'shopping/show-cart.html')
