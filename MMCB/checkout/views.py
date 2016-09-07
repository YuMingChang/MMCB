from django.shortcuts import render


def checkout_page(request):
    context = {
        'title': '結帳清單',
    }
    return render(request, 'checkout/checkout-page.html', context)
