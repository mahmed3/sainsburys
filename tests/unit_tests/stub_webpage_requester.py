import os

# Stub web page requester - returns contents from files on local disk
class StubWebPageRequester:
    PRODUCTS_PAGE = "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html"
    RESOURCES_PATH = os.path.join(os.path.dirname(__file__), 'resources/')

    def retrieve_webpage(self, url):
        if url == StubWebPageRequester.PRODUCTS_PAGE:
            return self.read_file('%s5_products.html' % StubWebPageRequester.RESOURCES_PATH)
        else:
            return self.read_file('%ssainsburys-apricot-ripe---ready-320g.html' % StubWebPageRequester.RESOURCES_PATH)

    def read_file(self, path):
        return open(path, 'r').read()
