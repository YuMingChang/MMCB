# -*- coding: utf-8 -*-
from django.contrib import admin
from products.models import Product, Detail, Images


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    raw_id_fields = ('product', )
    list_display = ['id', 'product', 'color', 'size', 'price', 'stock', 'sold']
    search_fields = ['id', 'product__name', ]


class DetailInline(admin.TabularInline):
    model = Detail
    extra = 1


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    raw_id_fields = ('product', )
    list_display = ['id', 'product', 'image', ]


class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date', 'is_display', 'thumbnail', ]
    list_editable = ['is_display', ]
    list_filter = ['is_display', 'date', ]
    search_fields = ['id', 'name', ]
    ordering = ('-date', )
    # fieldsets = ['name']
    inlines = [DetailInline, ImagesInline]
    fields = ('thumbnail', )
    readonly_fields = ('thumbnail', )

# Django admin model 漢化顯示文字: http://lishiguang.iteye.com/blog/1328986
