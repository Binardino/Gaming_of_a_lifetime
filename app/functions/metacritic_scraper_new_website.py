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
        #init empty console_dict as end result
        console_dict = {}
