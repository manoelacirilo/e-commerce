import sys

from app import app
from e_commerce.model import db
from e_commerce.model.cart import Cart
from e_commerce.model.item import Item
from e_commerce.schema import ma

port = 5100

if sys.argv.__len__() > 1:
    port = sys.argv[1]

print("Api running on port : {} ".format(port))

item = Item()
cart = Cart()


def main():
    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=port)


if __name__ == '__main__':
    main()
