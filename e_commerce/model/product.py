from e_commerce.model import db


class Product(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(50))
    price = db.Column('price', db.Float)
    items = db.relationship('Item', backref='product', lazy=True)

    def __str__(self) -> str:
        return self.__name

    def __repr__(self):
        return f'<Product(id={self.id}, name={self.name} price={self.price})>'
