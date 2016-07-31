import os
import sys

sys.path.append(os.getcwd())
sys.path.append(os.pardir)

from sainsburys.dao.products_dao import ProductsDao
from sainsburys.products_processor import ProductsProcessor
from sainsburys.request.webpage_requester import WebPageRequester
from sainsburys.service.products_service import ProductsService


# Retrieves product information and prints it to the console
def main():
    products_service = ProductsService(ProductsDao(WebPageRequester()))
    products = products_service.get_products()
    results = ProductsProcessor().process(products)
    print(results)


if __name__ == '__main__':
    main()
