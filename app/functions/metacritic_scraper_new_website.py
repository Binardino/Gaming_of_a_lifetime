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
    
    
    for index, card in enumerate(product_cards, start=1):
        title_elem =card.find('div', class_='c-finderProductCard_info').find('h3', class_='c-finderProductCard_titleHeading')
        game_title = title_elem.text.strip() if title_elem else "Title not found"
    
        release_date_elem = card.find('div', class_='c-finderProductCard_meta').find_all('span')[0]
        game_release_date = release_date_elem.text.strip() if release_date_elem else "Release date not found"
    
        rating_elem = card.find('div', class_='c-finderProductCard_meta').find_all('span')[2]
        rating = rating_elem.text.strip() if rating_elem else "Rating not found"
    
        description_elem = card.find('div', class_='c-finderProductCard_description')
        game_summary = description_elem.text.strip() if description_elem else "Description not found"
    
        # badge_img_elem = card.find('img', class_='c-finderProductCard_mustImage')
        # metascore_elem = badge_img_elem.find_parent('div') if badge_img_elem else None
        # metascore = metascore_elem.text.strip() if metascore_elem else "Metascore not found"
        metascore_elem = card.find('span', {'data-v-4cdca868': True})
        metascore = metascore_elem.text.strip() if metascore_elem else "Metascore not found"
    
    
    
        # metascore_elem = card.find('div', class_='c-siteReviewScore').find('span', class_='data-v-4cdca868')
        # metascore_span = metascore_elem.find('span') if metascore_elem else None
        # metascore = metascore_span.text.strip() if metascore_span else "Metascore not found"
    
        print(f"Game {index}: {game_title}")
        print(f"Release Date: {game_release_date}")
        print(f"Rating: {rating}")
        print(f"Metascore: {metascore}")
        print(f"Description: {game_summary}")
        print("\n")
        
        game_dict[game_title] = {
            'game_title'        : game_title,
           # 'game_platform'     : game_platform,
            'game_release_date' : game_release_date,
            'metascore'         : metascore,
            'game_summary'      : game_summary
        }
        
        #check if next page exist
        next_item = next_page_button = soup.find('span', {'class': 'c-navigationPagination_item--next'})
        if next_item and 'enabled' in next_page_button.get('class', []):
            print(next_item.next_element)
            page +=1
            time.sleep(1)
        else:
            #console_dict[console] = game_dict
            has_next_page = False