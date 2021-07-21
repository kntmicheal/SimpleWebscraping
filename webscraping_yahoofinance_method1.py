import requests
#from bs4 import beautifulSoup
from bs4 import BeautifulSoup 
import pandas as pd

stock_url = "https://finance.yahoo.com/most-active"
r = requests.get(stock_url)
data = r.text
soup = BeautifulSoup(data)


codes=[]
names=[]
prices=[]
changes=[]
percent_changes=[]
total_volumes=[]
market_caps=[]
price_earning_ratios=[]

stock_table= soup.find('tbody')
#print(stock_table)

for listing in stock_table.find_all('tr'):
#  print(listings)
  #code = listings.find('td',attrs={'aria-label':Sysmbol})
  #codes.append(code.text)
    code = listing.find('td', attrs={'aria-label':'Symbol'})
    codes.append(code.text)

    name = listing.find('td', attrs={'aria-label':'Name'})
    names.append(name.text)

    price = listing.find('td', attrs={'aria-label':'Price (Intraday)'})
    prices.append(price.text)
    
    # TODO: Use the same method as above to extract the remaining columns
    change = listing.find('td', attrs={'aria-label':'Change'})
    changes.append(change.text)
    
    percent_change = listing.find('td', attrs={'aria-label':'% Change'})
    percent_changes.append(percent_change.text)
    
    total_volume = listing.find('td', attrs={'aria-label':'Volume'})
    total_volumes.append(total_volume.text)
    
    market_cap = listing.find('td', attrs={'aria-label':'Market Cap'})
    market_caps.append(market_cap.text)
    
    price_earning_ratio = listing.find('td', attrs={'aria-label':'PE Ratio (TTM)'})
    price_earning_ratios.append(price_earning_ratio.text)


    df = pd.DataFrame({"Symbol":                codes, 
                    "Name":                  names, 
                    "Price":                 prices, 
                    "Change":                changes, 
                    "% Change":              percent_changes, 
                    "Market Cap":            market_caps, 
                    "Volume":                total_volumes, 
                    "PE Ratio (TTM)":        price_earning_ratios})
df