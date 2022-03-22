from flask_sqlalchemy import SQLAlchemy

from e_commerce.model.item import Item


class ItemRepository:

    def __init__(self, db):
        self.db: SQLAlchemy = db

    def add(self, **kwargs):
        item = Item(quantity=kwargs['quantity'], product_id=kwargs['product_id'], cart_id=kwargs['cart_id'])

        try:
            self.db.session.add(item)
            self.db.session.commit()

            return item
        except Exception as e:
            raise e

    def get_all(self):
        return self.db.session.query(Item).all()

    def get_cart(self, item_id):
        return self.db.session.query(Item).get_or_404(item_id)
