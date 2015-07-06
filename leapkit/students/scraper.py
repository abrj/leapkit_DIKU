import urllib2
import urllib
from bs4 import BeautifulSoup

class Scraper():

    def __init__(self, headers):
        self.headers = headers

    def scrape(self, url):
        try:

            if not(not("http://" in url) and not("https://" in url)):
                url = url.replace("http://","").replace("https://","")
            url = urllib.quote(url.encode('utf-8'))
            url = "https://" + url

            req = urllib2.Request(url, headers=self.headers)
            return  BeautifulSoup(urllib2.urlopen(req).read())
        except urllib2.URLError:
            print "connection Timed out"
            return None
