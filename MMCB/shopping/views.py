from django.urls import reverse
from django.shortcuts import render, redirect

from carton.cart import Cart
from products.models import Detail


def add(request):
    cart = Cart(request.session)
    selitem_id = request.GET.get('id')
    selitem_qty = request.GET.get('quantity')
    selitem = Detail.objects.get(id=selitem_id)
    cart.add(selitem, selitem_qty, price=selitem.price)
    return redirect(reverse('store') + "#No{}Card".format(selitem.product.id))


def remove(request):
    cart = Cart(request.session)
    selitem = Detail.objects.get(id=request.GET.get('id'))
    cart.remove(selitem)
    return redirect(reverse('cart:shopping-cart-show'))


def clear(request):
    cart = Cart(request.session)
    cart.clear()
    return redirect(reverse('cart:shopping-cart-show'))


def show(request):
    cart = Cart(request.session)
    errors = []
    isLessThanStock = False
    if request.method == 'POST':
        quantitylist = request.POST.getlist('quantity[]')
        for idx, item in enumerate(cart.products):
            item = Detail.objects.get(id=item.id)
            if (item.stock < int(quantitylist[idx])):
                cart.set_quantity(item, item.stock)
                errors.append('{}({})  商品庫存少於所選擇數量，自動幫您降為商品庫存所剩'.format(item.product, item))
                isLessThanStock = True
            else:
                cart.set_quantity(item, quantitylist[idx])
        if isLessThanStock:
            return render(request, 'shopping/show-cart.html', {'errors': errors})
        else:
            return redirect(reverse('checkout:page'))

    return render(request, 'shopping/show-cart.html')
