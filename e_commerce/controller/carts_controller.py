from flask import Blueprint
from flask_restful import Resource, reqparse

from e_commerce.service.cart_service import CartService

blueprint = Blueprint('carts_controller', __name__)


class CartsController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(reqparse.Argument('product_id', store_missing=False))
    parser.add_argument(reqparse.Argument('quantity', store_missing=False))

    # parser.add_argument(reqparse.Argument('password', store_missing=False))

    @staticmethod
    @blueprint.route('/add_to_cart', methods=['POST'])
    def add_to_cart():
        # { 'product_id': 22, 'quantity': 1 }
        args = CartsController.parser.parse_args()
        cart = CartService.add_to_cart(args['product_id'], args['quantity'])
