class Product:
    def __init__(self, title, size, unit_price, description):
        self.title = title
        self.size = size
        self.unit_price = unit_price
        self.description = description

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
