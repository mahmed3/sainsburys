from sainsburys.products_processor import ProductsProcessor
from sainsburys.service.products_service import ProductsService


def main():
    print("Sainsbury’s Software Engineering Test")
    print("> Retrieving products...")
    products = ProductsService().get_products()
    print("Retrieved", len(products), "products")
    print("> Processing products...")
    results = ProductsProcessor().process(products)
    print(results)
    print("> Done")

if __name__ == '__main__':
    main()