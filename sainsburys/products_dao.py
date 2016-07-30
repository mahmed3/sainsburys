from bs4 import BeautifulSoup
import urllib.request

from sainsburys.basic_product_info import BasicProductInfo


class ProductsDao(object):
    def retrieve_webpage(self, url):
        return urllib.request.urlopen(url).read()

    def extract_items(self, webpage):
        contents = BeautifulSoup(webpage, "html.parser")
        products_html = contents.find_all("div", class_="productInner")
        products = []
        for product_html in products_html:
            product_title = self.extract_product_title(product_html)
            unit_price = self.extract_unit_price(product_html)
            products.append(BasicProductInfo(product_title, unit_price))
        return products

    def extract_product_title(self, product_html):
        return product_html.find('div', class_='productInfo').h3.a.text.strip()

    def extract_unit_price(self, product_html):
        unit_price = product_html.find('p', class_='pricePerUnit').text.strip()
        unit_price = unit_price.replace(";/unit", "")
        unit_price = unit_price.replace("&pound", "")
        unit_price = float(unit_price)
        return unit_price
