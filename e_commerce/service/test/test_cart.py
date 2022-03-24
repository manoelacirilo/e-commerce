import unittest

from flask import Flask
from flask_testing import TestCase

from e_commerce.model import db
from e_commerce.service.cart_service import CartService
from e_commerce.service.product_service import ProductService
from e_commerce.service.user_service import UserService


class TestCart(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://manoelacirilo:1907@localhost/e_commerce_test'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)
        app.app_context().push()
        return app

    def setUp(self):
        db.create_all()
        self.user = UserService.sign_up(name='Usertest', email='Emailtest', password='Passwordtest')
        self.product = ProductService.register(name='bag', price=100)

    def test_should_add_to_cart(self):
        """
        Should create cart and add product
        """

        # given happens on setUp
        # when
        cart = CartService.add_to_cart(product_id=self.product.id, quantity=10, user_id=self.user.id)

        # then
        self.assertEqual(cart.items[0].quantity, 10)
        self.assertEqual(cart.user, self.user)
        self.assertEqual(cart.items[0].product, self.product)

    def test_should_add_to_existing_cart(self):
        """
        Should add product to existing cart, if cart exists
        """

        # given
        product2 = ProductService.register(name='shoes', price=150)

        created_cart = CartService.add_to_cart(product_id=self.product.id, quantity=10, user_id=self.user.id)

        # when
        existing_cart = CartService.add_to_cart(product_id=product2.id, quantity=5, user_id=self.user.id)

        # then
        self.assertEqual(existing_cart.id, created_cart.id)

        self.assertEqual(existing_cart.items[0].quantity, 10)
        self.assertEqual(existing_cart.items[0].product, self.product)

        self.assertEqual(existing_cart.items[1].quantity, 5)
        self.assertEqual(existing_cart.items[1].product, product2)

    def test_should_raise_error_if_invalid_product(self):
        """
        Should raise ValueError if product doesn't exist on database
        """
        invalid_product_id = 99

        with self.assertRaises(ValueError) as context:
            CartService.add_to_cart(product_id=invalid_product_id, quantity=5, user_id=self.user.id)

        self.assertTrue('Product not found' in str(context.exception))

    def test_should_raise_error_if_invalid_quantity(self):
        """
        Should raise ValueError if quantity is invalid
        """
        invalid_quantity = 0

        with self.assertRaises(ValueError) as context:
            CartService.add_to_cart(product_id=self.product.id, quantity=invalid_quantity, user_id=self.user.id)

        self.assertTrue('Invalid quantity' in str(context.exception))

    def test_should_raise_error_if_invalid_user(self):
        """
        Should raise ValueError if user doesn't exist on database
        """
        invalid_user_id = 99

        with self.assertRaises(ValueError) as context:
            CartService.add_to_cart(product_id=self.product.id, quantity=2, user_id=invalid_user_id)

        self.assertTrue('User not found' in str(context.exception))

    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
