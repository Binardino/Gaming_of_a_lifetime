import requests
from fake_useragent import UserAgent
import json


class HLTBRequests_post:
    def create_headers():
        ua = UserAgent()
        headers = {'Accept-Language': 'en-US,en;q=0.8',
                   'Upgrade-Insecure-Requests': '1',
                   'content-type': 'application/json',
                   'User-Agent': ua.random.strip()
            }
        return headers

    def get_hltb_game_data(game_list):
    url = 'https://howlongtobeat.com/api/search'
    
    
    game_list = df_vg['game_name'].sample(10)
    
    game_dict = {}
    for game_name in game_list:
    #game_name = 'Horizon Forbidden West'
        
        headers = create_headers()
