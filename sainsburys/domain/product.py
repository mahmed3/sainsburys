
'''
    Product represents all the information about a product.
    Including: title, unit price, description, and the size of the product's details page
'''
class Product:
    def __init__(self, title, details_page_size, unit_price, description):
        self.title = title
        self.size = details_page_size
        self.unit_price = unit_price
        self.description = description

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
