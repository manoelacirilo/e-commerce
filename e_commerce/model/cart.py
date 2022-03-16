from e_commerce.model import db


class Cart(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    items = db.relationship('Item', backref='cart', lazy=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
