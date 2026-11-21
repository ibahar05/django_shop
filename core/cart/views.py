from django.http import JsonResponse
from django.views.generic import View, TemplateView

from .cart import CartSession


class SessionAddProductView(View):
    def post(self, request, *args, **kwargs):
        try:
            product_id = int(request.POST.get("product_id"))
        except (TypeError, ValueError):
            return JsonResponse({"error": "invalid product_id"}, status=400)

        cart = CartSession(request.session, request.user)
        cart.add_product(product_id)
        return JsonResponse({
            "cart": cart.get_cart_dict(),
            "total_quantity": cart.get_total_quantity(),
        })


class SessionUpdateProductQuantityView(View):
    def post(self, request, *args, **kwargs):
        try:
            product_id = int(request.POST.get("product_id"))
            quantity = int(request.POST.get("quantity"))
        except (TypeError, ValueError):
            return JsonResponse({"error": "invalid input"}, status=400)

        cart = CartSession(request.session, request.user)
        if quantity > 0:
            cart.update_product_quantity(product_id, quantity)
        else:
            cart.remove_product(product_id)
        return JsonResponse({
            "cart": cart.get_cart_dict(),
            "total_quantity": cart.get_total_quantity(),
        })


class SessionRemoveProductView(View):
    def post(self, request, *args, **kwargs):
        try:
            product_id = int(request.POST.get("product_id"))
        except (TypeError, ValueError):
            return JsonResponse({"error": "invalid product_id"}, status=400)

        cart = CartSession(request.session, request.user)
        cart.remove_product(product_id)
        return JsonResponse({
            "cart": cart.get_cart_dict(),
            "total_quantity": cart.get_total_quantity(),
        })


class CartSummaryView(TemplateView):
    template_name = "cart/cart-summary.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartSession(self.request.session, self.request.user)
        context["cart_items"] = cart.get_items()
        context["total_quantity"] = cart.get_total_quantity()
        context["total_payment_price"] = cart.get_total_payment_price()
        return context