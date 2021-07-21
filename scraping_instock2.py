import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


base_url = "https://www.thewhiskyexchange.com" 

product_links =[]
def create_productlinks(base_url):
    for x in range(1,3):
        
        r = requests.get(f'https://www.thewhiskyexchange.com/c/33/american-whiskey?pg={x}&psize=24&sort=ldesc',headers = headers)
        soup =BeautifulSoup(r.content,'lxml')
        product_link = soup.find_all('div',class_ ='product-list')
        return product_link
print(create_productlinks(base_url))