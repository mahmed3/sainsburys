import unittest

from sainsburys.products_processor import ProductsProcessor


class ProductsProcessorTest(unittest.TestCase):
    def setUp(self):
        self.products_processor = ProductsProcessor()
        self.products = []

    def test_sum_unit_prices(self):
        sum = self.products_processor.sum_unit_prices(self.products)
        self.assertEqual(sum, 0)

    def test_products_to_json(self):
        json = self.products_processor.products_to_json(self.products)
        self.assertIsNotNone(json)
