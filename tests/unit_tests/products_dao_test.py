import unittest

from sainsburys.basic_product_info import BasicProductInfo
from sainsburys.products_dao import ProductsDao


class ProductsDaoTest(unittest.TestCase):
    def setUp(self):
        self.products_dao = ProductsDao()
        self.webpage = open('resources/5_products.html', 'r').read()

    def test_extract_items(self):
        items = self.products_dao.extract_items(self.webpage)
        self.assertEqual(len(items), 7)
        self.assertEqual(items[0].title, "Sainsbury's Apricot Ripe & Ready x5")
        self.assertEqual(items[0].unit_price, 3.50)


if __name__ == '__main__':
    unittest.main()
