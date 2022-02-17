import unittest

from e_commerce.model.product import Product


class TestProduct(unittest.TestCase):

    def test_register(self):
        product = Product.register(name='bag', price=10.0)

        self.assertEqual(product.name, 'bag')
        self.assertEqual(product.price, 10.0)
        self.assertEqual(product.id, Product.counter)

    def test_invalid_register(self):
        with self.assertRaises(ValueError) as context:
            Product.register(name='', price=-1)

        self.assertTrue('Invalid product data' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
