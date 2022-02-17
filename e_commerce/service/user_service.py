import bcrypt

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
        return bcrypt.hashpw(password.encode('utf8'), salt)

    # def login(self, email: str, password: str) -> str:
    #     if email == self.__email and self.check_password(password):
    #         self.logged = True
    #         return f'Welcome {self.__name}'
    #     else:
    #         raise ValueError('Invalid credentials')
    #
    # def check_password(self, password_to_check: str) -> bool:
    #     return bcrypt.checkpw(password_to_check.encode('utf8'), self.__password)
    #
    # def profile(self) -> str:
    #     if self.logged:
    #         return f'Id: {self.id}\nName: {self.__name}\nEmail: {self.__email}'
    #     raise ValueError('Unauthorized')
