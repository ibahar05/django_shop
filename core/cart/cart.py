from shop.models import ProductModel, ProductStatusType
from .models import *

class CartSession:
    total_payment_price = 0
    def __init__(self, session, user=None):
        self.session = session
        self.user = user
        self._cart = self.session.setdefault("cart",
                                     {
                                         'items':[],
                                         'total_price':0,
                                         'total_items':0
                                     })


    def update_product_quantity(self, product_id, quantity):
        for item in self._cart["items"]:
            if product_id == item["product_id"]:
                item["quantity"] = quantity
                break
        self.save()



    def add_product(self, product_id):
        for item in self._cart["items"]:
            if product_id == item["product_id"]:
                item["quantity"] += 1
                break
        else:
            new_item = {"product_id":product_id,
                            "quantity" : 1
                            }
            self._cart["items"].append(new_item)
        self.save()

    def remove_product(self, product_id):
        for item in self._cart["items"]:
            if product_id == item["product_id"]:
                self._cart["items"].remove(item)
                break

        self.save()


    def clear(self):
        self._cart = self.session["cart"] = {"items": []}
        self.save()

    def get_cart_dict(self):
        return self._cart
    
    def get_items(self):
        self.total_payment_price = 0
        total_items = 0
        result = []
        for item in self._cart["items"]:
            product_obj = ProductModel.objects.filter(
                id=item["product_id"], status=ProductStatusType.publish.value
            ).first()
            if not product_obj:
                continue
            total = int(item["quantity"]) * product_obj.get_price()
            self.total_payment_price += total
            total_items += item["quantity"]
            result.append({**item, "product_obj": product_obj, "total_price": total})

        self._cart["total_price"] = self.total_payment_price
        self._cart["total_items"] = total_items
        self.session.modified = True
        return result

    def get_total_payment_price(self):
        return self.total_payment_price
            

    def get_total_quantity(self):
        # total_quantity = 0
        # for item in self._cart["items"]:
        #     total_quantity += item["quantity"]
        # return total_quantity
        return len(self._cart["items"])

    

    def merge_session_cart_in_db(self, user):

        cart, _ = CartModel.objects.get_or_create(user=user)

        for item in self._cart["items"]:
            db_item, created = CartItemModel.objects.get_or_create(
                cart=cart,
                product_id=item["product_id"],
                defaults={"quantity": item["quantity"]},
            )
            if not created:
                db_item.quantity += item["quantity"]   
                db_item.save()


        self._cart["items"] = [
            {"product_id": ci.product_id, "quantity": ci.quantity}
            for ci in cart.cart_items.all()
        ]
        self.save()


    def sync_to_db(self, user):
      
        cart, _ = CartModel.objects.get_or_create(user=user)
        product_ids = [item["product_id"] for item in self._cart["items"]]


        cart.cart_items.exclude(product_id__in=product_ids).delete()

        for item in self._cart["items"]:
            CartItemModel.objects.update_or_create(
                cart=cart,
                product_id=item["product_id"],
                defaults={"quantity": item["quantity"]},
            )

    def save(self):
        self.session.modified = True
        if self.user and self.user.is_authenticated:
            self.sync_to_db(self.user)

