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
#%%
class HTMLRequests_metacritic:
    def create_headers():
        """
        returns random web User Agent as headers to scrap web content
        """
        ua = UserAgent()
        headers = {'Accept-Language': 'en-US,en;q=0.8',
                   'Upgrade-Insecure-Requests': '1',
                   'content-type': 'application/json',
                   'User-Agent': ua.random.strip()
            }
        return headers
#%%
class metacritic_data_fetcher:
    def create_metacritic_dict(console_list):
        """
        input  : list of console to scrap metacritic score
        output : dictionary of consoles with all games' metascore
        """    
        #init empty console_dict as end result
        console_dict = {}
        for console in console_list:
            print("calling f{console} to scrap")
            page = 1
            has_next_page = True
            game_dict = {}
            while has_next_page:
                print(f"----------------- querying {console}  -----  page {page}")
                url = f'https://www.metacritic.com/browse/game/{console}/all/all-time/metascore/?releaseYearMin=1958&releaseYearMax=2025&platform={console}&page={page}'
                print(url)
                #calling url with headers
                headers = HTMLRequests_metacritic.create_headers()
                response = requests.get(url, headers=headers)
                print(response.status_code)
                if response.status_code != 200:
                    has_next_page = False
                    console_dict[console] = game_dict
                    continue
                elif response.status_code == 200:
                    # Get the HTML content
                    html_content = response.text
                    soup = BeautifulSoup(html_content, 'html.parser')
                
                    # Find all product cards
                    product_cards = soup.find_all('div', class_='c-finderProductCard-game')
                    navigation = soup.find_all('div', class_='c-navigationPagination u-flexbox u-flexbox-alignCenter u-flexbox-justifyCenter g-outer-spacing-top-large g-outer-spacing-bottom-large u-text-center g-outer-spacing-bottom-medium-fluid')
                    #iteration through each scraped item
                    for index, card in enumerate(product_cards, start=1):
                        #fetch item from h3 beacon
                        title_elem =card.find('div', class_='c-finderProductCard_info').find('h3', class_='c-finderProductCard_titleHeading')
                        game_title = title_elem.text.strip() if title_elem else "Title not found"
                        #fetch release data from div
                        release_date_elem = card.find('div', class_='c-finderProductCard_meta').find_all('span')[0]
                        game_release_date = release_date_elem.text.strip() if release_date_elem else "Release date not found"
                        #fetch description  data from div
                        description_elem = card.find('div', class_='c-finderProductCard_description')
                        game_summary = description_elem.text.strip() if description_elem else "Description not found"
                        # fetch metascore from title attribute
                        metascore_div = card.find('div', title=re.compile(r'^Metascore \d+ out of 100'))
                        if metascore_div:
                            title_attr = metascore_div.get('title')
                            metascore_match = re.search(r'Metascore (\d+) out of 100', title_attr)
                            metascore = metascore_match.group(1) if metascore_match else "Metascore not found"
                        else:
                            metascore = "Metascore not found"
                    
                        print(f"Game {index}: {game_title}")
                        print(f"Release Date: {game_release_date}")
                        print(f"Metascore: {metascore}")
                        print(f"Description: {game_summary}")
                        print("\n")
                        #add game to game dict
                        game_dict[game_title] = {
                                'game_title'        : game_title,
                                'game_release_date' : game_release_date,
                                'metascore'         : metascore,
                                'game_summary'      : game_summary
                                                }
                        
                    #check if next page exist
                    next_page_button = soup.find('span', {'class': 'c-navigationPagination_item--next'})
                    if next_page_button and 'enabled' in next_page_button.get('class', []):
                        #print(next_page_button.next_element)
                        page +=1
                        time.sleep(45)
                    else:
                        #end of loop for console - add all games console_dict[console] key
                        console_dict[console] = game_dict
                        has_next_page = False

            
        return console_dict

#%%
if __name__ == "__main__":        
    #test_dict = metacritic_data_fetcher.create_metacritic_dict(['ps4','ps5','nintendo-switch','pc'])
    test_dict2 = metacritic_data_fetcher.create_metacritic_dict(['nintendo-switch'])
    
    #%%
test_dict3 = test_dict | test_dict2

import json

# Convert and write JSON object to file
with open("dic_meta.json", "w") as outfile: 
    json.dump(test_dict3, outfile)