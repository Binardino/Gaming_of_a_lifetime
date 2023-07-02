import requests
from fake_useragent import UserAgent
import json
import pandas as pd

class HLTBRequests_post:
    def create_headers():
        ua = UserAgent()
        headers = {'Accept-Language': 'en-US,en;q=0.8',
                   'Upgrade-Insecure-Requests': '1',
                   'content-type': 'application/json',
                   'User-Agent': ua.random.strip(),
                    'referer': url
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
    
    
    def get_hltb_game_data(df):
        url = 'https://howlongtobeat.com/api/search'
        
        
        game_list = df['game_name'].sample(10)
        
        game_dict = {}
        for game_name in game_list:
        #game_name = 'Horizon Forbidden West'
            
            headers = HLTBRequests_post.create_headers()
            print(headers)
            
            payload = HLTBRequests_post.create_payloads(game_name)
            print(payload)
            r = requests.post(url, headers=headers, data=payload)
            
            print(r.status_code)
        
            game_temp = json.loads(r.text)
            
            game_dict[game_name] = game_temp
            
        return game_dict

