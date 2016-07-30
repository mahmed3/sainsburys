from sainsburys.request.abstract_webpage_requester import AbstractWebPageRequester
from tests.unit_tests import test_utils


class StubWebPageRequester(AbstractWebPageRequester):
    PRODUCTS_PAGE = "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html"

    def retrieve_webpage(self, url):
        if url == StubWebPageRequester.PRODUCTS_PAGE:
            return test_utils.read_file('tests/unit_tests/resources/5_products.html')
        else:
            return test_utils.read_file('tests/unit_tests/resources/sainsburys-apricot-ripe---ready-320g.html')
