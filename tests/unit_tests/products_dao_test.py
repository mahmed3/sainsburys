import unittest

from sainsburys.products_dao import ProductsDao


class ProductsDaoTest(unittest.TestCase):
    def setUp(self):
        self.products_dao = ProductsDao()
        self.webpage = open('resources/5_products.html', 'r').read()

    def test_extract_items(self):
        items = self.products_dao.extract_items(self.webpage)
        self.assertIsNotNone(items)


if __name__ == '__main__':
    unittest.main()
