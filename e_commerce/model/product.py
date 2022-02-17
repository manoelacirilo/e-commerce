from e_commerce.model import db


class Product(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    _name = db.Column('name', db.String(50))
    _price = db.Column('price', db.Float)

    def __init__(self, name: str, price: float) -> None:
        self.__name: str = name
        self.__price: float = price

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def id(self) -> int:
        return self.__id
