import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd




headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


#print(soup)

#products_range = []

#for x in range(1,10):
base_url = "https://www.thewhiskyexchange.com/c/33/american-whiskey?pg=1&psize=24&sort=ldesc"
session = requests.get(base_url)
soup = BeautifulSoup(session.text,'lxml')
name = soup.find_all('h3')
n=len(name)
for x in range(n): 
        print(str.strip(name[x].text))


#brands = soup.find("div",class_ ="product-list")
  #products_range.append(brand)
#s = HTMLSession()
#r = s.get(base_url)
#sel ='div > h3'
#print(r.html.find(sel))

#links = r.html.find(sel) 
#products_range = []
#for t in links:
    #name = t.find('h3', {'class':'product-main__name'}).text.strip()
    
     #products_range.append(t.attrs['h3'])

print(len(name))
#print(soup)


  

