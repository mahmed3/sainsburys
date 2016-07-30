from bs4 import BeautifulSoup
import urllib.request

class ProductsDao(object):
    def retrieve_webpage(self, url):
        return urllib.request.urlopen(url).read()

    def extract_items(self, webpage):
        contents = BeautifulSoup(webpage, "html.parser")
        # extract items from contents
        return contents
