from sainsburys.dao.products_dao import ProductsDao
from sainsburys.domain.product import Product


class ProductsService():
    def __init__(self):
        self.products_page = "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html"
        self.products_dao = ProductsDao()

    def get_products(self):
        webpage = self.products_dao.retrieve_webpage(self.products_page)
        basic_products_info = self.products_dao.extract_basic_product_info(webpage)
        products = []
        for basic_product_info in basic_products_info:
            details_page = self.products_dao.retrieve_webpage(basic_product_info.details_url)
            product_details = self.products_dao.extract_detailed_product_info(details_page)
            product = Product(basic_product_info.title, product_details.size, basic_product_info.unit_price, product_details.description)
            products.append(product)
        return products