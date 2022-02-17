from flask_restful import Resource, reqparse

from e_commerce.schema.user_schema import user_schema, users_schema
from e_commerce.service.user_service import UserService


class UsersController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')
    parser.add_argument('email')
    parser.add_argument('password')

    @staticmethod
    def get():
        users = UserService.get_users()
        return users_schema.dump(users)

    @staticmethod
    def post():
        try:
            args = UsersController.parser.parse_args()
            user = UserService.sign_up(name=args['name'], email=args['email'], password=args['password'])
            return user_schema.dump(user), 201
        except Exception as e:
            return {'error': str(e)}, 400
