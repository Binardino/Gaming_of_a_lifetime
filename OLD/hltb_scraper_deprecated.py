import requests
from fake_useragent import UserAgent
import json
import pandas as pd
#%% import data
#@st.cache_data
def get_data_csv(path):
    return pd.read_csv(path)

#st.cache_data
def get_data_sql(query, engine):
    return pd.read_sql(query=query, con=engine)

df_vg = get_data_csv('../db_data/csv/df_vg_local_csv.csv')

url = 'https://howlongtobeat.com/api/search'


game_list = df_vg['game_name'].sample(10)

game_dict = {}
for game_name in game_list:
#game_name = 'Horizon Forbidden West'
    
    ua = UserAgent()
    headers = {'Accept-Language': 'en-US,en;q=0.8',
           'Upgrade-Insecure-Requests': '1',
           'content-type': 'application/json',
           'User-Agent': ua.random.strip(),
           'referer': url
    }
    
    payload_r = {
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
                        'modifier': search_modifiers.value,
                    },
                    'users': {
                        'sortCategory': "postcount"
                    },
                    'filter': "",
                    'sort': 0,
                    'randomizer': 0
                }
            }
    
    payload = json.dumps(payload_r)
    
    r = requests.post(url, headers=headers, data=payload)
    
    print(r.status_code)

    game_temp = json.loads(r.text)
    
    game_dict[game_name] = game_temp

#%%
dicohours = {}

for key, value in dico_yoyo.items():
    #print(value)
    game_name = key
    
    #get value from sub dict data
    data_list = value['data']

