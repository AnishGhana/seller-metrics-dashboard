from django.contrib import admin

from .models import Product, Sale


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "unit_price", "inventory", "reorder_level")
    list_filter = ("category",)


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "sale_price", "sold_on")
    list_filter = ("sold_on", "product__category")
