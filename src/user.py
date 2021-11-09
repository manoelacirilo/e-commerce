import bcrypt


class User:
    counter = 0

    def __init__(self, name, email, password):
        self.__id = User.counter + 1
        self.__name = name
        self.__email = email
        self.__password = User.__encrypt_password(password)
        self.__logged = False
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

    def login(self, email, password):
        if email == self.__email and self.check_password(password):
            self.__logged = True
            print(f'Welcome {self.__name}')
        else:
            print('Invalid credentials')

    def check_password(self, password_to_check):
        return bcrypt.checkpw(password_to_check.encode('utf8'), self.__password)

    def is_logged(self):
        return self.__logged
