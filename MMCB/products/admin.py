from django.contrib import admin
from products.models import Product, Images, Item


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    raw_id_fields = ('product', )
    list_display = [
        'id',
        'product',
        'image',
    ]


class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    raw_id_fields = ('product', )
    list_display = [
        'id',
        'product',
        'style',
        'size',
        'price',
        'selling',
        'selling_volume',
        'reset_time',
        'is_shortage',
    ]
    list_editable = ['is_shortage', ]
    search_fields = ['id', 'product__name', ]


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'onshelf_time',
        'is_display',
        'freight_only',
        'thumbnail',
    ]
    list_editable = ['is_display', 'freight_only', ]
    list_filter = ['onshelf_time', 'is_display', 'freight_only', ]
    search_fields = ['id', 'name', ]
    ordering = ('-onshelf_time', )
    inlines = [ImagesInline, ItemInline]
    readonly_fields = ('thumbnail', )

# Django admin model 漢化顯示文字: http://lishiguang.iteye.com/blog/1328986
# Django Admin Show Image from Imagefield: http://stackoverflow.com/questions/16307307/django-admin-show-image-from-imagefield
