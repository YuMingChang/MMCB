from django.contrib import admin
from checkout.models import PurchaseOrder


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'shopper',
        'order_date',
        'get_sold_goods',
        'freight',
        'total',
        'status',
    )
    list_filter = ('status', 'order_date', )
    search_fields = ('shopper', )
    ordering = ('-order_date', 'total', )
