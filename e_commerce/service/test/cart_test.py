import unittest

from flask import Flask
from flask_testing import TestCase

from e_commerce.model import db
from e_commerce.service.cart_service import CartService
from e_commerce.service.product_service import ProductService
from e_commerce.service.user_service import UserService


class CartTest(TestCase):

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

    def test_should_add_to_cart(self):
        # given
        user = UserService.sign_up(name='Usertest', email='Emailtest', password='Passwordtest')
        product = ProductService.register(name='bag', price=100)

        # when
        cart = CartService.add_to_cart(product_id=product.id, quantity=10, user_id=user.id)

        # then
        self.assertEqual(cart.items[0].quantity, 10)
        self.assertEqual(cart.user, user)
        self.assertEqual(cart.items[0].product, product)

    def test_should_add_to_existing_cart(self):
        # given
        user = UserService.sign_up(name='Usertest', email='Emailtest', password='Passwordtest')
        product1 = ProductService.register(name='bag', price=100)
        product2 = ProductService.register(name='shoes', price=150)

        created_cart = CartService.add_to_cart(product_id=product1.id, quantity=10, user_id=user.id)

        # when
        existing_cart = CartService.add_to_cart(product_id=product2.id, quantity=5, user_id=user.id)

        # then
        self.assertEqual(existing_cart.id, created_cart.id)

        self.assertEqual(existing_cart.items[0].quantity, 10)
        self.assertEqual(existing_cart.items[0].product, product1)

        self.assertEqual(existing_cart.items[1].quantity, 5)
        self.assertEqual(existing_cart.items[1].product, product2)

    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()