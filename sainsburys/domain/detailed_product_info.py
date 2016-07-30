class DetailedProductInfo:
    def __init__(self, size, description):
        self.size = size
        self.description = description

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
