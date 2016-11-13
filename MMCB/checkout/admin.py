from django.contrib import admin
from checkout.models import PurchaseOrder


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    raw_id_fields = ['buyer']
    list_display = (
        'number',
        'buyer',
        'order_time',
        'get_sold_goods',
        'freight',
        'total',
        'status',
        'remittance_time',
        'shipment_time',
        'renounce_time',
    )
    list_filter = ('buyer', 'status', 'order_time', )
    search_fields = ('buyer', )
    ordering = ('-order_time', '-total', )
