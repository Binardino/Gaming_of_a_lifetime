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
    game_rows = soup.select('tableclam-list tr')

    game_dict = {}

    for row in game_rows:

    return gameè
    