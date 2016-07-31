import unittest

from sainsburys.domain.product import Product
from sainsburys.products_processor import ProductsProcessor


class ProductsProcessorTest(unittest.TestCase):
    def setUp(self):
        self.products_processor = ProductsProcessor()
        self.products = [Product("Prod1", "Size1", 1.2, "Desc1"), Product("Prod2", "Size2", 3.4, "Desc2")]

    def test_process_products_returns_expected_response(self):
        actual = self.products_processor.process_products(self.products)
        self.assertEqual(actual, self.get_expected())

    def get_expected(self):
        results = [
            {"title": "Prod1", "size": "Size1", "unit_price": 1.2, "description": "Desc1"},
            {"title": "Prod2", "size": "Size2", "unit_price": 3.4, "description": "Desc2"}
        ]
        return {"results": results, "total": 4.6}
