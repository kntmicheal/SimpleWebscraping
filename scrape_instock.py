import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd




headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

base_url = "https://www.thewhiskyexchange.com"

s = HTMLSession()

products_range = []


def create_productlink(base_url):
    for x in range(1,3):
       r = s.get(f'https://www.thewhiskyexchange.com/c/33/american-whiskey?pg={x}&psize=24&sort=ldesc')
       sel ='div > ul > li > a'
       name = r.html.find(sel)
       for links in name:
          product_link = links.attrs['href']
          products_range.append(base_url + product_link )
    return products_range

create_productlink(base_url)

all_list = []

for linkz in products_range:
  r =s.get(linkz)
 
  
  try:
    p_name = r.html.find('h1.product-main__name',first=True).text.strip()
    p_price = r.html.find('p.product-action__price',first=True).text.strip()
    #in_stock = r.html.find('p >i[aria-hidden = "True"] ',first=True).text.strip()
    if r.html.find('p >i[aria-hidden = "True"] ') is not None:
      in_stock = 'Available'


    #print(p_name)
  except:
    p_name = ""
    p_price = ""
    in_stock = "Unvailable"

  p_list={'p_name' : p_name,
          'p_price' :p_price,
          'in_stock':in_stock
          }
  all_list.append(p_list)
  #print('sick:',p_list['p_name'])
df = pd.DataFrame(all_list)
print(df)

