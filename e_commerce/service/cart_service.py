from e_commerce.repository import cart_repository, item_repository


class CartService:
    @staticmethod
    def add_to_cart(product_id, quantity, user_id):
        cart = cart_repository.get_by_user_id(user_id)

        if not cart:
            cart = cart_repository.add(user_id=user_id)

        item_repository.add(quantity=quantity, product_id=product_id, cart_id=cart.id)

        return cart
