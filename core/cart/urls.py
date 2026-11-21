from django.urls import path, include
from . import views

app_name = "cart"

urlpatterns = [
    path("session/add_product/",views.SessionAddProductView.as_view(),name="session-add-product"),
    path("session/update_product/quantity/",views.SessionUpdateProductQuantityView.as_view(),name="update-product-quantity"),
    path("session/delete_product/",views.SessionRemoveProductView.as_view(),name="remove-product"),
    path("session/cart/summary/",views.CartSummaryView.as_view(),name="cart-summary")
]
