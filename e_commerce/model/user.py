from sqlalchemy import UniqueConstraint

from e_commerce.model import db


# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
class User(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(50), nullable=False)
    email = db.Column('email', db.String(50), nullable=False)
    password = db.Column('password', db.LargeBinary(60), nullable=False)
    carts = db.relationship('Cart', backref='user', lazy=True)
    __table_args__ = (UniqueConstraint('email', name='_email_uc'),)

    def __str__(self) -> str:
        return f'<User(id={self.id}, name={self.name} email={self.email})>'

    def __repr__(self):
        return f'<User(id={self.id}, name={self.name} email={self.email})>'
