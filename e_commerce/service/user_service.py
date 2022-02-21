import bcrypt
from flask import current_app
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer)

# from e_commerce.model.user import User
from e_commerce.repository import user_repository


class UserService:

    @staticmethod
    def sign_up(name: str, email: str, password: str):
        if name == '' or email == '' or password == '':
            raise ValueError('Registration not done')

        return user_repository.add(
            name=name,
            email=email,
            password=UserService.__encrypt_password(password)
        )

    @staticmethod
    def __encrypt_password(password: str) -> bytes:
        salt: bytes = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    @staticmethod
    def get_users():
        return user_repository.get_all()

    @staticmethod
    def get_user(user_id):
        return user_repository.get_user(user_id)

    @staticmethod
    def authenticate_user(email, password):
        user = user_repository.get_user_by_email(email)
        if not user or not UserService.__check_password(password_to_check=password, user_password=user.password):
            raise ValueError('Email or Password Invalid')
        return UserService.__generate_auth_token(user.id)

    @staticmethod
    def __check_password(password_to_check: str, user_password: bytes) -> bool:
        return bcrypt.checkpw(password_to_check.encode('utf-8'), user_password)

    @staticmethod
    def __generate_auth_token(user_id, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': user_id})

    # def login(self, email: str, password: str) -> str:
    #     if email == self.__email and self.check_password(password):
    #         self.logged = True
    #         return f'Welcome {self.__name}'
    #     else:
    #         raise ValueError('Invalid credentials')

    #
    # def profile(self) -> str:
    #     if self.logged:
    #         return f'Id: {self.id}\nName: {self.__name}\nEmail: {self.__email}'
    #     raise ValueError('Unauthorized')
