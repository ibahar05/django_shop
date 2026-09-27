from django.db import models
from decimal import Decimal


class ProductStatusType(models.IntegerChoices):
    publish = 1, "فعال"
    draft = 2, "غیر فعال"


class ProductCategoryModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductModel(models.Model):
    category = models.ManyToManyField(ProductCategoryModel)
    title = models.CharField(max_length=250)
    slug = models.SlugField(allow_unicode=True)
    image = models.ImageField(
        default="/default/product-image.png", upload_to="product/img/"
    )
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    status = models.IntegerField(
        choices=ProductStatusType.choices, default=ProductStatusType.draft.value
    )
    price = models.DecimalField(max_digits=10, decimal_places=0)
    discount_percent = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_price(self):     
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        return '{:,}'.format(round(discounted_amount))

    def is_discounted(self):
        return self.discount_percent != 0

    class Meta:
        ordering = ["-created_date"]


class ProductImageModel(models.Model):
    product = models.ForeignKey("shop.ProductModel", on_delete=models.CASCADE)
    file = models.ImageField(upload_to="product/extra-img/")

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
