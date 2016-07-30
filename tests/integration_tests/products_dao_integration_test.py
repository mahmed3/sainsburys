import unittest

from sainsburys.products_dao import ProductsDao


class ProductsDaoTest(unittest.TestCase):
    def setUp(self):
        self.products_dao = ProductsDao()
        self.url = "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html"

    def test_retrieve_webpage(self):
        webpage_contents = self.products_dao.retrieve_webpage(self.url)
        self.assertGreater(len(webpage_contents), 0)


if __name__ == '__main__':
    unittest.main()
