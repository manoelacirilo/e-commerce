from e_commerce.model.cart import Cart
from e_commerce.schema import ma
from e_commerce.schema.item_schema import ItemSchema


class CartSchema(ma.Schema):
    class Meta:
        fields = ("id", "items", "items_count", "subtotal")
        model = Cart

    items = ma.Nested(ItemSchema, many=True)


cart_schema = CartSchema()
carts_schema = CartSchema(many=True)
