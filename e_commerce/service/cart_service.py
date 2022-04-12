from e_commerce.model.cart import Cart
from e_commerce.repository import cart_repository, item_repository, product_repository, user_repository


class CartService:
    @staticmethod
    def add_to_cart(product_id: int, quantity: int, user_id: int) -> Cart:
        """
        Adds product to cart by creating item and cart (if it doesn't exist)
        :param product_id: int
        :param quantity: int
        :param user_id: int
        :return: Cart
        """
        if quantity < 1:
            raise ValueError('Invalid quantity')

        product = product_repository.get_product(product_id)
        if not product:
            raise ValueError('Product not found')

        CartService._find_user(user_id)

        cart = cart_repository.get_by_user_id(user_id)
        if not cart:
            cart = cart_repository.add(user_id=user_id)

        item = item_repository.get_item_by_product_and_cart(product_id, cart.id)
        if item:
            new_quantity = quantity + item.quantity
            item_repository.edit_item(item.id, quantity=new_quantity)
        else:
            item_repository.add(quantity=quantity, product_id=product_id, cart_id=cart.id)

        return cart

    @staticmethod
    def get_cart(user_id):
        CartService._find_user(user_id)

        return cart_repository.get_by_user_id(user_id)

    @staticmethod
    def _find_user(user_id):
        user = user_repository.get_user_silent(user_id)
        if not user:
            raise ValueError('User not found')
