import requests
#from bs4 import beautifulSoup
from bs4 import BeautifulSoup 
import pandas as pd




def scrape_table(url):
    soup = BeautifulSoup(requests.get(url).text)
    headers = [header.text for listing in soup.find_all('thead') for header in listing.find_all('th')]
    raw_data = {header:[] for header in headers}

    for rows in soup.find_all('tbody'):
      for row in rows.find_all('tr'):
        if len(row) != len(headers): continue
        for idx, cell in enumerate(row.find_all('td')):
          raw_data[headers[idx]].append(cell.text)

    return pd.DataFrame(raw_data)
