from e_commerce.model.product import Product
from e_commerce.schema import ma


class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "price")
        model = Product


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
