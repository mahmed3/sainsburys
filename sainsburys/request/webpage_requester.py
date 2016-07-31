import urllib.request

# WebPageRequester retrieves the contents at a given URL
class WebPageRequester:
    def retrieve_webpage(self, url):
        return urllib.request.urlopen(url).read()
