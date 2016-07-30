import urllib.request

from sainsburys.request.abstract_webpage_requester import AbstractWebPageRequester


class WebPageRequester(AbstractWebPageRequester):
    def retrieve_webpage(self, url):
        return urllib.request.urlopen(url).read()
