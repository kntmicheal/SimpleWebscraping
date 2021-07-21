import requests
from bs4 import BeautifulSoup
import pandas as pd



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}


def parse_url(url):
    r = requests.get(url)
    data = BeautifulSoup(r.text,'html.parser')
    raw_data =""
    return raw_data