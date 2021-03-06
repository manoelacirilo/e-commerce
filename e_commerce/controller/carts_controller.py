from flask import Blueprint
from flask_restful import Resource, reqparse

from e_commerce.controller import auth
from e_commerce.schema.cart_schema import cart_schema
from e_commerce.service.cart_service import CartService

blueprint = Blueprint('carts_controller', __name__)


class CartsController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(reqparse.Argument('product_id', store_missing=False, type=int))
    parser.add_argument(reqparse.Argument('quantity', store_missing=False, type=int))

    @staticmethod
    @blueprint.route('/add_to_cart', methods=['POST'])
    @auth.login_required
    def add_to_cart():
        try:
            args = CartsController.parser.parse_args()
            cart = CartService.add_to_cart(args['product_id'], args['quantity'], auth.current_user().id)
            return cart_schema.dump(cart), 201
        except Exception as e:
            return {'error': str(e)}, 400

    @staticmethod
    @blueprint.route('/get_cart', methods=['GET'])
    @auth.login_required
    def get_cart():
        try:
            cart = CartService.get_cart(user_id=auth.current_user().id)
            return cart_schema.dump(cart), 200
        except Exception as e:
            return {'error': str(e)}, 400

