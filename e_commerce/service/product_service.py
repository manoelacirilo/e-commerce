from e_commerce.repository import product_repository


class ProductService:
    @staticmethod
    def register(name: str, price: float):
        if name == '' or price < 0.0:
            raise ValueError('Invalid product data')

        return product_repository.add(
            name=name,
            price=price
        )

    @staticmethod
    def get_products():
        return product_repository.get_all()

    @staticmethod
    def get_product(product_id):
        return product_repository.get_product(product_id)
