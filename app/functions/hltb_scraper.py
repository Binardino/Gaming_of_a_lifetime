import requests
from fake_useragent import UserAgent
import json
import pandas as pd
import sys
import os
#set path for dynamic function import
sys.path.append("..")
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
from app.functions.metacritic_scraper import *


class HLTBRequests_post:
    def create_headers(url):
        """

        Parameters
        ----------
        url : URL of endpoint to call

        Returns
        -------
        headers : dict with headers required for HLTB requests call - set up JSON content, language, & user agent

        """
        ua = UserAgent()
        headers = {'Accept-Language': 'en-US,en;q=0.8',
                   'Upgrade-Insecure-Requests': '1',
                   'content-type': 'application/json',
                   'User-Agent': ua.random.strip(),
                    'referer': url
            }
        return headers

    def create_payloads(game_name, platform, search_modifier=''):
        """

        Parameters
        ----------
        game_name : TYPE
            DESCRIPTION.
        search_modifier : str
            How Long To Beat search bar allows you to input variable for game
                #NONE - fetch all data 
                    NONE = "" - 
                # ISOLATE_DLC shows only DLC in the search result
                    ISOLATE_DLC = "only_dlc"
                # HIDE_DLC hide DLCs in the search result
                    HIDE_DLC = "hide_dlc"
            DESCRIPTION. The default is ''

        Returns
        -------
        payload : TYPE
            DESCRIPTION.
        payload to input in the How Long To Beat API call

        """
        #console mapper to match API naming
        console_mapper = { 'PS1':'PlayStation' ,'PS2':'PlayStation 2', 'PS3':'PlayStation 3','PS4':'PlayStation 4', 'PS5':'PlayStation 5',
                          'Switch':'Nintendo Switch','GameCube':'Nintendo GameCube', 'N64':'Nintendo 64', 'SNES': 'Super Nintendo', 'NES':'NES','GameBoy':'GameBoy','GBA': 'Game Boy Advance', 'Wii':'Wii',                          
                          'Megadrive': 'Sega Mega Drive/Genesis',
                          'Android':'Mobile', 'PC':'PC'}
        
        platform = console_mapper[platform]
        
        #payload creation
        payload_raw = {
                    'searchType': "games",
                    'searchTerms': game_name.split(),
                    'searchPage': 1,
                    'size': 20,
                    'searchOptions': {
                        'games': {
                            'userId': 0,
                            'platform': platform,
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
                            'modifier': search_modifier,
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
    
    
    def get_hltb_game_data2(df, search_modifier):
        """

        Parameters
        ----------
        df : DataFrame of list of videogames
        
        search_modifier : param for HLTB API : choice to include or exclude game's DLC data

        Returns
        -------
        game_dict : dict of games with all raw HLTB data for matched data from input df

        """
        url = 'https://howlongtobeat.com/api/search'
        
#        df['console'] = df['console'].str.replace(' / ', '', regex=False)
        df['console'] = df['console'].apply(lambda x : x.split('|')[0])
        # df['console2'] = df['console'].str.split(pat='|')
        #df['console'] = df['console'].apply(lambda x : console_mapper[x])
        #df['console'] = df['console'].replace(console_mapper)

        game_dict = {}
        #for each game in df vg, do API call and fetch HLTB data
        for idx, game in df.iterrows():
            print(f"\n ####### \n ------------------ \n calling game : {game['game_name']}\n ------------------  \n ####### ")
            #custom header per call
            headers = HLTBRequests_post.create_headers(url)
            print(headers)
            #call API on game name + console
            #wip need to check missing data
            payload = HLTBRequests_post.create_payloads(game['game_name'], game['console'], search_modifier)
            print(payload)
            r = requests.post(url, headers=headers, data=payload)
            print(r.status_code)
        
            game_temp = json.loads(r.text)
            #add API response to return game_dict 
            game_dict[game['game_name']] = game_temp
            
        return game_dict

    
#%% import data
#@st.cache_data
def get_data_csv(path):
    return pd.read_csv(path)

#st.cache_data
def get_data_sql(query, engine):
    return pd.read_sql(query=query, con=engine)

df_vg = get_data_csv('../db_data/csv/df_vg_local_csv.csv')

df = df_vg

dico_yoyo = HLTBRequests_post.get_hltb_game_data(df_vg, 'hide_dlc')
#%%
class JSON_parser():
    def JSON_to_df(game_dict):
        """
        Parameters
        ----------
        game_dict : dict - raw data from HLTB API response

        Returns
        -------
        df_hltb : dataframe - dict transformed in raw df - ready for transformation

        """  
        dict_temp_htlb = {} 
        #iteration through each game name (ie. key) & game dic data (value)
        for key, value in dico_yoyo.items():
            print("key is", key, "\n ------------------  \n")

            #get value from sub dict data
            data_list = value['data']                
            for subgame_dict in data_list:
                #dict_parser
                # NB : all raw duration from API response are in seconds
                game_name  = subgame_dict['game_name']  #game_name
                game_id    = subgame_dict['game_id']  #game_name
                comp_100   = subgame_dict['comp_100'] #completionist 100%
                comp_all   = subgame_dict['comp_all'] #completing "All Styles" for HLTB
                comp_main  = subgame_dict['comp_main'] #complishing main story
                comp_plus  = subgame_dict['comp_plus'] #main story + side quests
                platform   = subgame_dict['profile_platform'] 
                developer  = subgame_dict['profile_dev']
                score      = subgame_dict['review_score']
                if 'release' in subgame_dict:
                    release    = subgame_dict['release'] #add release data if exists - missing in some dict
           
                dict_temp_htlb[key] = {'game_name' : game_name,
                                      'comp_100'   : comp_100,
                                      'comp_all'   : comp_all,
                                      'comp_main'  : comp_main,
                                      'comp_plus'  : comp_plus,
                                      'platform'   : platform,
                                      'developer'  : developer
                                     }
                  
        df_hltb = pd.DataFrame.from_dict(dict_temp_htlb, orient='index')
            
        return df_hltb
    
    
    def df_cleanser(df):
        
        
        return df_clean

            # for version in subgame_dict:
            #     best_match = None
            #     best_similarity = 0
            #     similarity = fuzzymatch_metacritic(df_vg, version)
            #     if similarity > best_similarity:
            #         best_similarity = similarity
            #         best_match = version
                    
            # if best_match is not None:
            #     print("Best Match - Game Name:", best_match.game_name)
            #     # Print other attributes of the best match if needed
            
      #      print(value['data'])
            
        return df_htlb
            
            print(value['data'])

