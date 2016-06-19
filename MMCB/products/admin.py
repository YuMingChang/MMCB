from django.contrib import admin
from .models import Product, Detail

# Register your models here.
# Django admin model 漢化顯示文字: http://lishiguang.iteye.com/blog/1328986

@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ['product', 'color', 'size', 'price']

class DetailInline(admin.TabularInline):
    model = Detail
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'raiser', 'date', 'is_display', 'image']
    inlines = [DetailInline]
