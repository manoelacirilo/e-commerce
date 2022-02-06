import unittest

from src.model.product import Product


class TestProduct(unittest.TestCase):

    def test_register(self):
        product = Product.register(name='bag', price=10.0)

        self.assertEqual(product.name, 'bag')
        self.assertEqual(product.price, 10.0)
        self.assertEqual(product.id, Product.counter)


if __name__ == '__main__':
    unittest.main()
