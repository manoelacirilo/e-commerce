from e_commerce.model.user import User
from e_commerce.schema import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email")
        model = User


user_schema = UserSchema()
users_schema = UserSchema(many=True)
