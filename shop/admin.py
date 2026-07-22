from django.contrib import admin
from .models import Product, Order, OrderItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")
    search_fields = ("name",)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ("unit_price",)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "created_at", "total")
    list_filter = ("status", "created_at")
    inlines = [OrderItemInline]

