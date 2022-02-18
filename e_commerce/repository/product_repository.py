from e_commerce.model.product import Product


class ProductRepository:

    def __init__(self, db):
        self.db = db

    def add(self, **kwargs):
        product = Product(name=kwargs['name'], price=kwargs['price'])

        try:
            self.db.session.add(product)
            self.db.session.commit()

            return product
        except Exception as e:
            raise e
