# Web Scraping to CSV

import csv
from urllib.request import urlopen
# in terminal "pip install beautifulsoup4"
from bs4 import BeautifulSoup

with open("Bradesco_8252022_112950 AM.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    print(soup.body.text)