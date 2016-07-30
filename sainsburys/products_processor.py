import json


class ProductsProcessor:
    def process(self, products):
        total = sum(map(lambda p: p.unit_price, products))
        results = [product.__dict__ for product in products]
        response = {"results": results, "total": total}
        return json.dumps(response)
