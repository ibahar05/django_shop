from django.contrib import admin
from shop.models import ProductModel, ProductCategoryModel, ProductImageModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "stock",
        "status",
        "price",
        "discount_percent",
        "created_date",
    )


@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_date")


@admin.register(ProductImageModel)
class ProductImageModelAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "created_date")
