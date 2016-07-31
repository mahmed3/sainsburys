import unittest

from sainsburys.request.webpage_requester import WebPageRequester


class WebPageRequesterIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.webpage_requester = WebPageRequester()
        self.url = "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html"

    def test_retrieve_webpage(self):
        webpage_contents = self.webpage_requester.retrieve_webpage(self.url)
        self.assertGreater(len(webpage_contents), 0)


if __name__ == '__main__':
    unittest.main()
