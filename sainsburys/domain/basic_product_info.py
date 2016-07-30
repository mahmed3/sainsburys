class BasicProductInfo:
    def __init__(self, title, unit_price, details_url):
        self.title = title
        self.unit_price = unit_price
        self.details_url = details_url

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
