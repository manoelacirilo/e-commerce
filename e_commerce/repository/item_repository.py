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

    def get_item(self, item_id):
        return self.db.session.query(Item).get_or_404(item_id)

    def get_item_by_product_and_cart(self, product_id, cart_id):
        return self.db.session.query(Item).filter_by(product_id=product_id, cart_id=cart_id).first()

    def edit_item(self, item_id, **kwargs):
        self.db.session.query(Item).filter_by(id=item_id).update(kwargs)
        self.db.session.commit()

        return self.get_item(item_id)
