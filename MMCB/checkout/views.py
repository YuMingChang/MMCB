from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from functools import reduce
from datetime import datetime
from carton.cart import Cart
from checkout.models import PurchaseOrder
from members.models import PersonalInfo
from products.models import Item


def checkout_page(request):
    errors = []
    cart = Cart(request.session)
    freight_only = any([item.product.product.freight_only for item in cart.items])
    cost_total = cart.total
    if cart.is_empty:
        return redirect(reverse('store'))
    else:
        if request.POST:
            cart_list = [v for k, v in cart.cart_serializable.items()]
            cal_price = reduce(lambda x, y: x + y, [i['quantity'] * int(i['price']) for i in cart_list])
            delivery = request.POST.get('delivery')
            try:
                shopper = PersonalInfo.objects.get(id=request.user.personalinfo.id)
                if cart.total == cal_price and delivery is not None:
                    order = PurchaseOrder.objects.create(
                        number=0,
                        buyer=shopper,
                        order_time=datetime.now(),
                        freight=0 if cart.total > 1500 else
                        60 if delivery.isdigit() else 90,
                        ship_method='FML' if delivery.isdigit() else 'KTJ',
                        address=delivery,
                        total=cart.total,
                        buyer_notes=request.POST.get('shopper_notes'),
                        order_notes=cart_list
                    )
                    order.number = float(datetime.now().strftime('%y%m%d%H%M%S')) + float(order.id)
                    order.total = order.total + order.freight

                    # 更改為預購模式！
                    for d in cart_list:
                        item = get_object_or_404(Item, id=d['product_pk'])
                        order.sold_goods.add(item)
                        item.pre_order += d['quantity']
                        # print ('id={} / 存貨={} / 售貨={} / 總售貨={}'.format(
                        #     item.id, item.stock,
                        #     item.sold, item.total_sold
                        # ))
                        item.save()
                    order.save()
                    cart.clear()
                    return HttpResponseRedirect(reverse('checkout:orderinfo'))
                else:
                    errors.append('資料有誤 或 尚未填寫，請重新整理再次一次')
            except Exception as e:
                print ('%s (%s)' % (e, type(e)))
    context = {
        'title': '結帳清單',
        'errors': errors,
        'cost_total': cost_total,
        'freight_only': freight_only,
    }
    return render(request, 'checkout/checkout-page.html', context)


def checkout_orderinfo(request):
    errors = []
    newest_order = None
    user_orderlist = request.user.personalinfo.purchaseorder_set.all()
    try:
        newest_orderid = user_orderlist.order_by('-order_time')[0].id
        newest_order = get_object_or_404(PurchaseOrder, id=newest_orderid)
    except:
        errors.append('無法取得訂單資料')
    context = {
        'title': '訂單資訊',
        'myorder': newest_order,
        'errors': errors,
    }
    return render(request, 'checkout/checkout-orderinfo.html', context)
