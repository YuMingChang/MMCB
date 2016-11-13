from django.urls import reverse
from django.shortcuts import render, redirect

from carton.cart import Cart
from products.models import Item


def add(request):
    cart = Cart(request.session)
    selitem_id = request.GET.get('id')
    selitem_qty = request.GET.get('quantity')
    selitem = Item.objects.get(id=selitem_id)
    cart.add(selitem, selitem_qty, price=selitem.price)
    return redirect(reverse('store') + "#No{}Card".format(selitem.product.id))


def remove(request):
    cart = Cart(request.session)
    selitem = Item.objects.get(id=request.GET.get('id'))
    cart.remove(selitem)
    return redirect(reverse('cart:shopping-cart-show'))


def clear(request):
    cart = Cart(request.session)
    cart.clear()
    return redirect(reverse('cart:shopping-cart-show'))


def show(request):
    cart = Cart(request.session)
    if request.method == 'POST':
        quantitylist = request.POST.getlist('quantity[]')
        for idx, item in enumerate(cart.products):
            item = Item.objects.get(id=item.id)
            cart.set_quantity(item, quantitylist[idx])
        return redirect(reverse('checkout:page'))
    return render(request, 'shopping/show-cart.html')
