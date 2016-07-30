import unittest

from sainsburys.dao.products_dao import ProductsDao


class ProductsDaoTest(unittest.TestCase):
    def setUp(self):
        self.products_dao = ProductsDao()
        self.products_webpage = read_file('resources/5_products.html')
        self.detailed_product_webpage = read_file('resources/sainsburys-apricot-ripe---ready-320g.html')

    def test_extract_basic_product_info(self):
        items = self.products_dao.extract_basic_product_info(self.products_webpage)
        #TODO check against actual list of 7 items
        self.assertEqual(len(items), 7)
        self.assertEqual(items[0].title, "Sainsbury's Apricot Ripe & Ready x5")
        self.assertEqual(items[0].unit_price, 3.50)
        self.assertEqual(items[0].details_url, "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/sainsburys-apricot-ripe---ready-320g.html")

    def test_extract_detailed_product_info(self):
        detailed_info = self.products_dao.extract_detailed_product_info(self.detailed_product_webpage)
        self.assertEqual(detailed_info.size, "39.2kb")
        self.assertEqual(detailed_info.description, "\nApricots\n\n\n\n")

def read_file(path):
    return open(path, 'r').read()

if __name__ == '__main__':
    unittest.main()
