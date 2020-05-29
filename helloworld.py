# import libraries
from bs4 import BeautifulSoup
import urllib.request
import csv
import smtplib

# specify the url
urlpage = 'https://www.boursorama.com/bourse/forum/1rPNANO/'
# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')
#print(soup)
results = soup.find_all('div', attrs = {'class' : 'c-faceplate__price' })
nanobiotix_price = results[0].contents[0].contents[0]


