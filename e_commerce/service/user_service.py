import bcrypt
from flask import current_app
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

from e_commerce.repository import user_repository


class UserService:

    @staticmethod
    def sign_up(name: str, email: str, password: str):
        if name == '' or email == '' or password == '':
            raise ValueError('Registration not done')

        encrypted_password = UserService.__encrypt_password(password)

        return user_repository.add(
            name=name,
            email=email,
            password=encrypted_password
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

        if not user:
            raise ValueError('Email or Password Invalid')

        password_ok = UserService.__check_password(password_to_check=password, user_password=user.password)

        if not password_ok:
            raise ValueError('Email or Password Invalid')

        return UserService.__generate_auth_token(user.id)

    @staticmethod
    def __check_password(password_to_check: str, user_password: bytes) -> bool:
        return bcrypt.checkpw(password_to_check.encode('utf-8'), user_password)

    @staticmethod
    def __generate_auth_token(user_id, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': user_id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token

        user = user_repository.get_user(data['id'])
        if not user:
            raise ValueError('Invalid token')

        return user

    @staticmethod
    def edit_profile(user_id, **kwargs):
        # kwargs = { 'name': 'Alesson', 'password': '0987' }
        if 'password' in kwargs:
            kwargs['password'] = UserService.__encrypt_password(kwargs['password'])
            # kwargs = {'name': 'Alesson', 'password': '012390129301293012930129301293'}

        return user_repository.edit_user(user_id, **kwargs)
