import urllib.request

from bs4 import BeautifulSoup

from sainsburys.domain.basic_product_info import BasicProductInfo
from sainsburys.domain.detailed_product_info import DetailedProductInfo


class ProductsDao(object):
    def retrieve_webpage(self, url):
        return urllib.request.urlopen(url).read()

    def extract_basic_product_info(self, webpage):
        contents = BeautifulSoup(webpage, "html.parser")
        products_html = contents.find_all("div", class_="productInner")
        products = []
        for product_html in products_html:
            product_title, url = self.extract_product_title(product_html)
            unit_price = self.extract_unit_price(product_html)
            products.append(BasicProductInfo(product_title, unit_price, url))
        return products

    def extract_detailed_product_info(self, webpage):
        size = "%.1fkb" % (len(webpage) / 1000) # Rounded to 1dp. (divide by 1024?)
        contents = BeautifulSoup(webpage, "html.parser")
        description = contents.find("div", class_="productText").text
        return DetailedProductInfo(size, description)

    def extract_product_title(self, product_html):
        item_link = product_html.find('div', class_='productInfo').h3.a
        title = item_link.text.strip()
        url = item_link.attrs['href']
        return title, url

    def extract_unit_price(self, product_html):
        unit_price = product_html.find('p', class_='pricePerUnit').text.strip()
        unit_price = unit_price.replace(";/unit", "")
        unit_price = unit_price.replace("&pound", "")
        unit_price = float(unit_price) #TODO decimal
        return unit_price
