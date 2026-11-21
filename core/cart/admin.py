# cart/admin.py
from django.contrib import admin
from .models import CartModel, CartItemModel

class CartItemInline(admin.TabularInline):
    model = CartItemModel
    extra = 0

@admin.register(CartModel)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ("user", "created_date", "updated_date")
    inlines = [CartItemInline]

@admin.register(CartItemModel)
class CartItemModelAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity")
