from flask_restful import reqparse, Resource

from e_commerce.schema.product_schema import product_schema
from e_commerce.service.product_service import ProductService


class ProductsController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')
    parser.add_argument('price', type=float)

    @staticmethod
    def post():
        try:
            args = ProductsController.parser.parse_args()
            product = ProductService.register(name=args['name'], price=args['price'])
            return product_schema.dump(product), 201
        except Exception as e:
            return {'error': str(e)}, 400
