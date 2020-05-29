import urllib as urllib
import bs4 as BeautifulSoup
urllib.request.urlopen('http://www.d8.tv/d8-series/pid6654-d8-longmire.html').read()
soup = BeautifulSoup.BeautifulSoup(html)
