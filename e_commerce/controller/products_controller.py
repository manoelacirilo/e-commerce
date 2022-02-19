from flask import Blueprint, jsonify
from flask_restful import reqparse, Resource

from e_commerce.schema.product_schema import product_schema, products_schema
from e_commerce.service.product_service import ProductService

blueprint = Blueprint('products_controller', __name__)


class ProductsController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')
    parser.add_argument('price', type=float)

    @staticmethod
    @blueprint.route('/products', methods=['POST'])
    def post():
        try:
            args = ProductsController.parser.parse_args()
            product = ProductService.register(name=args['name'], price=args['price'])
            return product_schema.dump(product), 201
        except Exception as e:
            return {'error': str(e)}, 400

    @staticmethod
    @blueprint.route('/products', methods=['GET'])
    def get_all():
        products = ProductService.get_products()
        return jsonify(products_schema.dump(products))

    @staticmethod
    @blueprint.route('/products/<product_id>', methods=['GET'])
    def get_one(product_id):
        product = ProductService.get_product(product_id)
        return product_schema.dump(product)
