# Imports
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
import sys
# adding Folder_2 to the system path
sys.path.append("..")
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
from app.functions.data_wrangling import *
from app.functions.metacritic_wrangling import *
from app.functions.visualisation_tools import *

#%%#%% import data
#@st.cache_data
def get_data_csv(path):
    return pd.read_csv(path)

#st.cache_data
def get_data_sql(query, engine):
    return pd.read_sql(query=query, con=engine)

df_vg = get_data_csv('../df_vg_local_csv.csv')

df_meta = get_data_csv('../../db_data/csv/metacritic_6900_games_22_Dec_2016_updated.csv')
st.write(df_vg)


st.set_page_config(page_title="page2")
#%% README
st.write("# Welcome to the Adventure of a Lifetime - Metacritic comparison🎮")

st.markdown("""The goal of this part is to compare personal data from my videogame_lifetime database with the data from Metacritic.
            
            **Compare data from Metacritic dataset**
            
            The available Metacritic dataset dates back from 2016;
            
            Remaing data past 2016 fetched through web scraping from metacritic webpage for set of consoles I played.
            Side notebook updated the 2016 dataset used & displayed here. Only the {df_vg.size}
            
            """)
#%% import data
df_meta['Name'].fillna('NaN', inplace=True)
# df_meta['fuzz'] = df_meta['Name'].apply(lambda x : fuzzymatch_metacritic(x, df_vg))

df_vg['fuzz'] = df_vg['game_name'].apply(lambda x : fuzzymatch_metacritic(x, df_meta['Name']))

# st.write(df_meta)
st.write(df_vg)

df_merge = pd.merge(df_vg, df_meta, how='inner', left_on='fuzz', right_on='Name')

st.write(df_merge)