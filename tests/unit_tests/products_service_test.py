import unittest

from sainsburys.dao.products_dao import ProductsDao
from sainsburys.domain.product import Product
from sainsburys.service.products_service import ProductsService
from tests.unit_tests.stub_webpage_requester import StubWebPageRequester


class ProductsServiceTest(unittest.TestCase):
    def setUp(self):
        self.products_service = ProductsService(ProductsDao(StubWebPageRequester()))

    def test_get_products(self):
        actual = self.products_service.get_products()
        self.assertEqual(len(actual), 7)
        self.assertEqual(actual[0], Product("Sainsbury's Apricot Ripe & Ready x5", "39.2kb", 3.5, "\nApricots\n\n\n\n"))
