import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd




headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

base_url = "https://www.thewhiskyexchange.com/c/33/american-whiskey?pg=1&psize=24&sort=ldesc"

s = HTMLSession()

products_range = []
for x in range(1,10):
    r = s.get(f'https://www.thewhiskyexchange.com/c/33/american-whiskey?pg={x}&psize=24&sort=ldesc')
    sel ='div > ul > li > a'
    #print(r.html.find(sel))
    name = r.html.find(sel)
    for links in name:
         print(links.attrs['href'])

