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

    def create_soup_request(url, headers):
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')


class metacritic_data_fetcher:
    def create_metacritic_dict(console_list):
        console_dict = {}
        for console in console_list:
            game_dict = {}
            page = 0
            has_next_page = True
            
            while has_next_page:
                print(f"----------------- querying {console} -----  page {page}")
                url = f'https://www.metacritic.com/browse/games/release-date/available/{console}/metascore?page={page}'
                print(url)
                headers = HTMLRequests_metacritic.create_headers()
                response = requests.get(url, headers=headers)
                print(response.status_code)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    #fetch data from tableclam html element
                    game_rows = soup.select('table.clamp-list tr')

                    # Iterate over each game row from soup element and extract the required information
                    for row in game_rows:
                        game_title = row.select_one("a.title h3").text.strip() if row.select_one('.title') else None
                        game_score = row.select_one('.metascore_w').text.strip() if row.select_one('.metascore_w') else None
                        game_user_score = row.select_one('.clamp-userscore').text.strip() if row.select_one('.clamp-userscore') else None
                        game_platform = row.select_one('.platform .data').text.strip() if row.select_one('.platform .data') else None
                        game_release_date = row.select_one('.clamp-details').text.strip() if row.select_one('.clamp-details') else None
                        game_summary = row.select_one('.summary').text.strip() if row.select_one('.summary') else None
                        
                        # unable to directly fetch date from HTML beacons
                        # need to extract date using regex
                        date_regex = r"([A-Za-z]+ \d{1,2}, \d{4})"
                        if game_release_date:
                            match = re.search(date_regex, game_release_date)
                            release_date = match.group(1) if match else ""
                            game_release_date = pd.to_datetime(release_date).date()
                        
                        # unable to directly fetch user_score from HTML beacons
                        # need to extract user_score using regex
                        userscore_regex = r"(?<=User Score:\n\n)\S+"
                        if game_user_score:
                            match = re.search(userscore_regex, game_user_score)
                            game_user_score = match.group() if match else ""
                        
    
                        # Create a dictionary entry for the game
                        game_dict[game_title] = {
                            'game_title'        : game_title,
                            'game_platform'     : game_platform,
                            'game_release_date' : game_release_date,
                            'metascore'         : game_score,
                            'user _score'       : game_user_score,
                            'game_summary'      : game_summary
                        }
                        
                        print("Title:",         game_title)
                        print("Gamescore:",     game_score)
                        print("Platform:",      game_platform)
                        print("Release Date:",  game_release_date)
                        #print("Summary:",      game_summary)
                
                    #check if next page exist
                    next_item = soup.select_one('span.flipper.next')
                    if next_item.next_element.get('href'):
                        print(next_item.next_element)
                        page +=1
                        time.sleep(1)
                    else:
                        console_dict[console] = game_dict
                        has_next_page = False
    
        return console_dict

if __name__ == "__main__":        
    test_dict = metacritic_data_fetcher.create_metacritic_dict(['ps5', 'switch'])