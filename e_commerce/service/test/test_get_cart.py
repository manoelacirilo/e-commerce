import unittest

from flask_testing import TestCase

from e_commerce.model import db
from e_commerce.service.cart_service import CartService
from e_commerce.service.product_service import ProductService
from e_commerce.service.test import create_test_app
from e_commerce.service.user_service import UserService


class TestGetCart(TestCase):

    def create_app(self):
        return create_test_app()

    def setUp(self):
        db.create_all()
        self.user = UserService.sign_up(name='Usertest', email='Emailtest', password='Passwordtest')
        self.product = ProductService.register(name='bag', price=100)

    def test_should_return_empty_cart(self):
        cart = CartService.get_cart(user_id=self.user.id)
        self.assertIsNone(cart)

    def test_should_return_cart(self):
        # given
        CartService.add_to_cart(product_id=self.product.id, quantity=1, user_id=self.user.id)

        # when
        cart = CartService.get_cart(user_id=self.user.id)

        # then
        self.assertEqual(cart.items[0].quantity, 1)
        self.assertEqual(cart.user, self.user)
        self.assertEqual(cart.items[0].product, self.product)

    def test_should_raise_error_if_invalid_user(self):
        invalid_user_id = 99

        with self.assertRaises(ValueError) as context:
            CartService.get_cart(user_id=invalid_user_id)

        self.assertTrue('User not found' in str(context.exception))

    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
