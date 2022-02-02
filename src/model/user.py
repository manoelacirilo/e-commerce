from typing import Optional

import bcrypt


class User:
    counter: int = 0

    def __init__(self, name: str, email: str, password: str) -> None:
        self.__id = User.counter + 1
        self.__name: str = name
        self.__email: str = email
        self.__password: bytes = User.__encrypt_password(password)
        self.__logged: bool = False
        User.counter = self.__id

    @staticmethod
    def sign_up(name: str, email: str, password: str) -> Optional['User']:
        if name == '' or email == '' or password == '':
            raise ValueError('Registration not done')

        client: User = User(name, email, password)

        return client

    @staticmethod
    def __encrypt_password(password: str) -> bytes:
        salt: bytes = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf8'), salt)

    def login(self, email: str, password: str) -> str:
        if email == self.__email and self.check_password(password):
            self.logged = True
            return f'Welcome {self.__name}'
        else:
            raise ValueError('Invalid credentials')

    def check_password(self, password_to_check: str) -> bool:
        return bcrypt.checkpw(password_to_check.encode('utf8'), self.__password)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email

    @property
    def logged(self) -> bool:
        return self.__logged

    @logged.setter
    def logged(self, new_logged: bool) -> None:
        self.__logged = new_logged

    def __str__(self) -> str:
        return self.__name
