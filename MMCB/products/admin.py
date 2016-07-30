# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Product, Detail

# Register your models here.
# Django admin model 漢化顯示文字: http://lishiguang.iteye.com/blog/1328986

@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'color', 'size', 'price']
    list_display_links = ['product',]
class DetailInline(admin.TabularInline):
    model = Detail
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'raiser', 'date', 'is_display', 'image']
    list_display_links = ['name',]
    list_editable = ['is_display']
    list_filter = ['is_display', 'date']
    search_fields = ['name',]
    ordering = ('date',)
    # fieldsets = ['name']
    inlines = [DetailInline]
