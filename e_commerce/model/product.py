from e_commerce.model import db


class Product(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(50))
    price = db.Column('price', db.Float)
