from sainsburys.domain.product import Product


class ProductsService:

    def __init__(self, product_dao):
        self.products_dao = product_dao

    def get_products(self):
        basic_products_info = self.products_dao.get_basic_products_info()
        products = [self.create_product(basic_product_info) for basic_product_info in basic_products_info]
        return products

    def create_product(self, basic_product_info):
        details = self.products_dao.get_product_details(basic_product_info.details_url)
        return Product(basic_product_info.title, details.size, basic_product_info.unit_price, details.description)
