import unittest

from sainsburys.dao.products_dao import ProductsDao
from sainsburys.domain.basic_product_info import BasicProductInfo
from sainsburys.domain.detailed_product_info import DetailedProductInfo
from tests.unit_tests.stub_webpage_requester import StubWebPageRequester


class ProductsDaoTest(unittest.TestCase):
    def setUp(self):
        self.products_dao = ProductsDao(StubWebPageRequester())
        self.expected_first_product = self.get_basic_product()

    def test_extract_basic_product_info(self):
        actual = self.products_dao.get_basic_products_info()
        self.assertEqual(len(actual), 7)
        self.assertEqual(actual[0], self.expected_first_product)

    def test_extract_detailed_product_info(self):
        actual = self.products_dao.get_product_details(self.expected_first_product.details_url)
        expected = DetailedProductInfo("39.2kb", "\nApricots\n\n\n\n")
        self.assertEqual(actual, expected)

    def get_basic_product(self):
        details_url = "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/" \
                      "2015_Developer_Scrape/sainsburys-apricot-ripe---ready-320g.html"
        return BasicProductInfo("Sainsbury's Apricot Ripe & Ready x5", 3.50, details_url)

if __name__ == '__main__':
    unittest.main()
