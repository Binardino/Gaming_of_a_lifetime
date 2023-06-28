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

    def create soup_request(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')


class metacritic_data_fetcher:
    def create metacritic_dict(soup):
    #fetch data from tableclam html element
    game_rows = soup.select('tableclam-list tr')

    game_dict = {}

    # Iterate over each game row from soup element and extract the required information
    for row in game_rows:
        game_title = row.select_one('.title').text.strip() if row.select_one('.title') else None
        game_score = row.select_one('.metascore_w').text.strip() if row.select_one('.metascore_w') else None
        game_user_score = row.select_one('.clamp-userscore').text.strip() if row.select_one('.clamp-userscore') else None
        game_platform = row.select_one('.platform .data').text.strip() if row.select_one('.platform .data') else None
        game_release_date = row.select_one('.clamp-details').text.strip() if row.select_one('.clamp-details') else None
        game_summary = row.select_one('.summary').text.strip() if row.select_one('.summary') else None
        
    