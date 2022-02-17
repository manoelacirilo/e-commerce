from flask_restful import Resource

from e_commerce.schema.user_schema import user_schema
from e_commerce.service.user_service import UserService


class UserController(Resource):

    @staticmethod
    def get(user_id):
        user = UserService.get_user(user_id)
        return user_schema.dump(user)
