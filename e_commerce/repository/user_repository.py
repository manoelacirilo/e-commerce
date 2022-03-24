# https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/

from e_commerce.model.user import User


class UserRepository:

    def __init__(self, db):
        self.db = db

    # INSERT INTO "user" (name, email, password) VALUES ('Milo', 'milo@gmail.com', '1234');
    def add(self, **kwargs):
        user = User(name=kwargs['name'], email=kwargs['email'], password=kwargs['password'])

        try:
            self.db.session.add(user)
            self.db.session.commit()

            return user
        except Exception as e:
            raise e

    # SELECT * FROM "user";
    def get_all(self):
        return self.db.session.query(User).all()

    # SELECT * FROM "user" WHERE id = 1;
    def get_user(self, user_id):
        return self.db.session.query(User).get_or_404(user_id)

    def get_user_silent(self, user_id):
        return self.db.session.query(User).get(user_id)

    # Select * from "user" where email = 'bla';
    def get_user_by_email(self, email):
        return self.db.session.query(User).filter_by(email=email).first()

    def edit_user(self, user_id, **kwargs):
        # { 'name': 'Alesson', 'password': 'iuhc9udcaiosdaosidj' }
        self.db.session.query(User).filter_by(id=user_id).update(kwargs)
        self.db.session.commit()

        return self.get_user(user_id)

# args = ['Milo', 'milo@gmail.com', '1234']
# name=args[0], email=args[1], password=args[2]

# kwargs = {'name': 'Milo', 'email': 'milo@gmail.com', 'password': '1234'}
# name=kwargs['name']
