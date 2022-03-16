from e_commerce.model import db


class Item(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    quantity = db.Column('quantity', db.Integer, nullable=False)
    product_id = db.Column('product_id', db.Integer, db.ForeignKey('product.id'), nullable=False)
    cart_id = db.Column('cart_id', db.Integer, db.ForeignKey('cart.id'), nullable=False)

# my_user = User(id=1)
# print(my_user.id) => 1

# my_cart = Cart(id=3, user_id=1)
# print(my_cart.id) => 3
# print(my_cart.user_id) => 1
# print(my_user.carts) => [my_cart]
# print(my_cart.user) => my_user
# print(my_cart.user.id) => 1

# my_item = Item(id=1, product_id=2, cart_id=3)
# my_item.cart
# my_cart.items => [my_item]
