from e_commerce.model.item import Item
from e_commerce.schema import ma
from e_commerce.schema.product_schema import ProductSchema


class ItemSchema(ma.Schema):
    class Meta:
        fields = ("id", "quantity", "product")
        model = Item

    product = ma.Nested(ProductSchema)


item_schema = ItemSchema()
items_schema = ItemSchema(many=True)
