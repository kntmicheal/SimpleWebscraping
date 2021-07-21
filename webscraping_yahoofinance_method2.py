import requests
#from bs4 import beautifulSoup
from bs4 import BeautifulSoup 
import pandas as pd

stock_url = "https://finance.yahoo.com/most-active"
r = requests.get(stock_url)
data = r.text
soup = BeautifulSoup(data)

raw_data={}
headers=[]
for header_row in soup.find_all('thead'):
  for header in header_row.find_all('th'):
     #print(header.text)
     raw_data[header.text]=[]
     headers.append(header.text)
for rows in soup.find_all('tbody'):
  for row in rows.find_all('tr'):
    for idx, cell in enumerate(row.find_all('td')):
      raw_data[headers[idx]].append(cell.text)

pd.DataFrame(raw_data)



