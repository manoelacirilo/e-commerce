from flask_sqlalchemy import SQLAlchemy

from e_commerce.model.cart import Cart


class CartRepository:

    def __init__(self, db):
        self.db: SQLAlchemy = db

    def add(self, **kwargs):
        cart = Cart(user_id=kwargs['user_id'])

        try:
            self.db.session.add(cart)
            self.db.session.commit()

            return cart
        except Exception as e:
            raise e

    def get_by_user_id(self, user_id):
        return self.db.session.query(Cart).filter_by(user_id=user_id).first()

    def get_all(self):
        return self.db.session.query(Cart).all()

    def get_cart(self, cart_id):
        return self.db.session.query(Cart).get_or_404(cart_id)
