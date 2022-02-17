import unittest

from main import populate_products


class TestMain(unittest.TestCase):

    def test_populate_products(self):
        first_product = populate_products()[0]
        self.assertEqual(first_product.name, 'Product-0')
        self.assertEqual(first_product.price, 10)


if __name__ == '__main__':
    unittest.main()
