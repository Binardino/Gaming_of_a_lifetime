from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import requests
import time
import csv
from bs4 import BeautifulSoup
import lxml
import html5lib
import pprint
import scipy as sp
import re
from fake_useragent import UserAgent


class HTMLRequests_metacritic:
    def create_headers():
        ua = UserAgent()
        headers = {'Accept-Language': 'en-US,en;q=0.8',
                   'Upgrade-Insecure-Requests': '1',
                   'content-type': 'application/json',
                   'User-Agent': ua.random.strip()
            }
        return headers
    

game_dict = {}
page = 1
has_next_page = True

while has_next_page:
    
    #url = f'https://www.metacritic.com/browse/game/ps4/all/all-time/metascore/?releaseYearMin=1958&releaseYearMax=2024&platform={console}&page={page}'
    url = f'https://www.metacritic.com/browse/game/ps4/all/all-time/metascore/?releaseYearMin=1958&releaseYearMax=2024&platform=ps4&page={page}'
    print(url)
    headers = HTMLRequests_metacritic.create_headers()
    
    response = requests.get(url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        # Get the HTML content
        html_content = response.text
        
        soup = BeautifulSoup(html_content, 'html.parser')
       
    # Find all product cards
    product_cards = soup.find_all('div', class_='c-finderProductCard-game')
    
    navigtaion = soup.find_all('div', class_='c-navigationPagination u-flexbox u-flexbox-alignCenter u-flexbox-justifyCenter g-outer-spacing-top-large g-outer-spacing-bottom-large u-text-center g-outer-spacing-bottom-medium-fluid')
    
    game_dict = {}
