import bcrypt


class User:
    counter = 0

    def __init__(self, name, email, password):
        self.__id = User.counter + 1
        self.__name = name
        self.__email = email
        self.__password = User.__encrypt_password(password)
        User.counter = self.__id

    @staticmethod
    def sign_up(name, email, password):
        if name == '' or email == '' or password == '':
            print('Registration not done')
            return

        client = User(name, email, password)
        print(f'User {client.__name} successfully registered.')
        return client

    @staticmethod
    def __encrypt_password(password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf8'), salt)
