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
            print('Registration not done')
            return

        client: User = User(name, email, password)
        print(f'User {client.__name} successfully registered.')
        return client

    @staticmethod
    def __encrypt_password(password: str) -> bytes:
        salt: bytes = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf8'), salt)

    def login(self, email: str, password: str) -> None:
        if email == self.__email and self.check_password(password):
            self.logged = True
            print(f'Welcome {self.__name}')
        else:
            print('Invalid credentials')

    def check_password(self, password_to_check: str) -> bool:
        return bcrypt.checkpw(password_to_check.encode('utf8'), self.__password)

    @property
    def logged(self) -> bool:
        return self.__logged

    @logged.setter
    def logged(self, new_logged: bool) -> None:
        self.__logged = new_logged
