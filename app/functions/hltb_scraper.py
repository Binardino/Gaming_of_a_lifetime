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

    def create_payloads(game_name):
        
        payload_raw = {
                    'searchType': "games",
                    'searchTerms': game_name.split(),
                    'searchPage': 1,
                    'size': 20,
                    'searchOptions': {
                        'games': {
                            'userId': 0,
                            'platform': "",
                            'sortCategory': "popular",
                            'rangeCategory': "main",
                            'rangeTime': {
                                'min': 0,
                                'max': 0
                            },
                            'gameplay': {
                                'perspective': "",
                                'flow': "",
                                'genre': ""
                            },
                            'modifier': '',
                        },
                        'users': {
                            'sortCategory': "postcount"
                        },
                        'filter': "",
                        'sort': 0,
                        'randomizer': 0
                    }
                }
        
        payload = json.dumps(payload_raw)
        
        return payload
    
    
    def get_hltb_game_data(game_list):
    url = 'https://howlongtobeat.com/api/search'
    
    
