import unittest

from sainsburys.service.products_service import ProductsService


class ProductsServiceTest(unittest.TestCase):
    def setUp(self):
        self.products_service = ProductsService()

    def test_get_products(self):
        products = self.products_service.get_products()
        self.assertEqual(len(products), 7)