from flask import Blueprint, jsonify
from flask_restful import Resource, reqparse

from e_commerce.controller import auth
from e_commerce.schema.user_schema import user_schema, users_schema
from e_commerce.service.user_service import UserService

blueprint = Blueprint('users_controller', __name__)


class UsersController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')
    parser.add_argument('email')
    parser.add_argument('password')

    @staticmethod
    @blueprint.route('/users', methods=['GET'])
    def get_all():
        users = UserService.get_users()
        return jsonify(users_schema.dump(users))

    @staticmethod
    @blueprint.route('/users', methods=['POST'])
    def post():
        try:
            args = UsersController.parser.parse_args()
            user = UserService.sign_up(name=args['name'], email=args['email'], password=args['password'])
            return user_schema.dump(user), 201
        except Exception as e:
            return {'error': str(e)}, 400

    @staticmethod
    @blueprint.route('/users/<user_id>', methods=['GET'])
    def get_one(user_id):
        user = UserService.get_user(user_id)
        return user_schema.dump(user)

    @staticmethod
    @blueprint.route('/users/login', methods=['POST'])
    def login():
        try:
            args = UsersController.parser.parse_args()
            token = UserService.authenticate_user(email=args['email'], password=args['password'])
            return {'token': token.decode('ascii')}
        except Exception as e:
            return {'error': str(e)}, 401

    @staticmethod
    @blueprint.route('/users/profile')
    @auth.login_required
    def profile():
        return {'test': 'one'}

    @staticmethod
    @auth.verify_token
    def verify_token(token):
        return UserService.verify_auth_token(token)
