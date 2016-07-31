import decimal

from bs4 import BeautifulSoup

from sainsburys.domain.basic_product_info import BasicProductInfo
from sainsburys.domain.details_page_info import DetailsPageInfo

'''
    ProductsDao provides methods to retrieve information from the products page, and the products' details pages.
    The actual web request is delegated to the supplied WebPageRequester.
    Once a page has been retrieved, the HTML is then inspected, and the relevant contents extracted.
'''
class ProductsDao:
    PRODUCTS_PAGE_URL = "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html"

    def __init__(self, webpage_requester):
        self.webpage_requester = webpage_requester

    def get_basic_products_info(self):
        contents = self.webpage_requester.retrieve_webpage(ProductsDao.PRODUCTS_PAGE_URL)
        return self.extract_basic_product_info(contents)

    def get_product_details(self, url):
        contents = self.webpage_requester.retrieve_webpage(url)
        return self.extract_details_page_info(contents)

    def extract_basic_product_info(self, webpage):
        contents = BeautifulSoup(webpage, "html.parser")
        products_html = contents.find_all("div", class_="productInner")
        return [self.create_basic_product_info(product_html) for product_html in products_html]

    def create_basic_product_info(self, product_html):
        product_title, url = self.extract_product_title(product_html)
        unit_price = self.extract_unit_price(product_html)
        return BasicProductInfo(product_title, unit_price, url)

    def extract_details_page_info(self, webpage):
        size = "%.1fkb" % (len(webpage) / 1000)  # Rounded to 1dp. (divide by 1024?)
        contents = BeautifulSoup(webpage, "html.parser")
        description = contents.find("div", class_="productText").text
        return DetailsPageInfo(size, description)

    def extract_product_title(self, product_html):
        item_link = product_html.find('div', class_='productInfo').h3.a
        title = item_link.text.strip()
        url = item_link.attrs['href']
        return title, url

    def extract_unit_price(self, product_html):
        unit_price = product_html.find('p', class_='pricePerUnit').text.strip().replace(";/unit", "")
        unit_price = unit_price.replace("&pound", "")
        unit_price = decimal.Decimal(unit_price)
        return unit_price
