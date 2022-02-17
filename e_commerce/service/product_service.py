from e_commerce.model.product import Product


class ProductService:
    @staticmethod
    def register(name: str, price: float) -> 'Product':
        if name == '' or price < 0:
            raise ValueError('Invalid product data')

        product: Product = Product(name, price)
        return product
