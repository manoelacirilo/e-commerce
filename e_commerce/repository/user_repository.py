from e_commerce.model.user import User


class UserRepository:

    def __init__(self, db):
        self.db = db

    # INSERT INTO user (name, email, password) VALUES ('Milo', 'milo@gmail.com', '1234');
    def add(self, **kwargs):
        user = User(name=kwargs['name'], email=kwargs['email'], password=kwargs['password'])

        try:
            self.db.session.add(user)
            self.db.session.commit()

            return user
        except Exception as e:
            raise e

    def get_all(self):
        return self.db.session.query(User).all()

    def get_user(self, user_id):
        return self.db.session.query(User).get(user_id)

# args = ['Milo', 'milo@gmail.com', '1234']
# name=args[0], email=args[1], password=args[2]

# kwargs = {'name': 'Milo', 'email': 'milo@gmail.com', 'password': '1234'}
# name=kwargs['name']
