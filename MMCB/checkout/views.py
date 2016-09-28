from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from functools import reduce
from datetime import datetime
from carton.cart import Cart
from checkout.models import PurchaseOrder
from members.models import PersonalInfo
from products.models import Detail


def checkout_page(request):
    errors = []
    cart = Cart(request.session)
    if cart.is_empty:
        return redirect('store')
    else:
        if request.POST:
            cart_list = [v for k, v in cart.cart_serializable.items()]
            cal_price = reduce(lambda x, y: x + y, [i['quantity'] * int(i['price']) for i in cart_list])
            delivery = request.POST.get('delivery')
            try:
                shopper = PersonalInfo.objects.get(PersonalInfo, id=request.user.personalinfo.id)
            except:
                shopper = None
            print (shopper is None)
            # if cart.total == cal_price and shopper is not None:
            #     order = PurchaseOrder.objects.create(
            #         number=0,
            #         shopper=get_object_or_404(PersonalInfo, id=request.user.personalinfo.id),
            #         order_date=datetime.now(),
            #         freight=60 if delivery == '7-11' else 80
            #                    if delivery == 'postoffice' else 120
            #                    if delivery == 'homedelivery' else 1000,
            #         total=cart.total,
            #         notes=request.POST.get('shopper_notes'),
            #         order_notes=cart_list
            #     )
            #     order.number = float(datetime.now().strftime('%y%m%d%H%M%S')) + float(order.id)
            #     order.total = order.total + order.freight
            #     for d in cart_list:
            #         order.sold_goods.add(Detail.objects.get(id=d['product_pk']))
            #     order.save()
            #     cart.clear()
            #     return HttpResponseRedirect(reverse('checkout:orderinfo'))
            # else:
            #     errors.append('資料有誤，請重新整理再次一次')
    context = {
        'title': '結帳清單',
        'errors': errors,
    }
    return render(request, 'checkout/checkout-page.html', context)


def checkout_orderinfo(request):
    newest_orderid = request.user.personalinfo.purchaseorder_set.all().order_by('-order_date')[0].id
    newest_order = PurchaseOrder.objects.get(id=newest_orderid)
    context = {
        'title': '訂單資訊',
        'myorder': newest_order,
    }
    return render(request, 'checkout/checkout-orderinfo.html', context)
