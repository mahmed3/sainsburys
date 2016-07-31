# DetailsPageInfo represents the pertinent information from a product details page
class DetailsPageInfo:
    def __init__(self, page_size, description):
        self.size = page_size
        self.description = description

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
