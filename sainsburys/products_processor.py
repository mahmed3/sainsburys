import simplejson as json

# Products Processor takes the list of Products and produces a JSON response
class ProductsProcessor:
    def process(self, products):
        response = self.process_products(products)
        return self.jsonify(response)

    def process_products(self, products):
        unit_price_sum = sum(map(lambda p: p.unit_price, products))
        results = [product.__dict__ for product in products]
        return {"results": results, "total": unit_price_sum}

    def jsonify(self, response):
        return json.dumps(response, use_decimal=True, sort_keys=True, indent=4)
