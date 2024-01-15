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
import sqlalchemy
from tqdm import tqdm
# adding Folder_2 to the system path
sys.path.append("..")
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
from functions.data_wrangling import *
from functions.metacritic_wrangling import *
from functions.visualisation_tools import *
import functions.db_connection as db_co

st.set_page_config(page_title="page2 - Metacritic analysis")
#%%#%% import data
driver   = os.environ.get("POSTGRES_DRIVER")
user     = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
table    = os.environ.get("POSTGRES_META_TABLE")
database = os.environ.get("POSTGRES_META_DB")
host     = os.environ.get("POSTGRES_HOST")
port     = os.environ.get("CONTAINER_PORT")

#connection_string = f'{driver}//{user}:{password}@{host}:{port}/{database}'
connection_string = f'{driver}//{user}:{password}@{host}:5432/{database}'
print("connection_string is :", connection_string)

engine_vg_old = sqlalchemy.create_engine(connection_string)

engine_vg = db_co.sql_connection()

query = sqlalchemy.text('SELECT * FROM metacritic')
print(pd.read_sql(sql=query, con=engine_vg.connect()))
df_meta = db_co.get_data_sql(sql=query, engine=engine_vg.connect())

query = sqlalchemy.text('SELECT * FROM gaming_lifetime')
df_vg = db_co.get_data_sql(sql=query, engine=engine_vg.connect())
#st.write(df_vg)
#%% README
st.write(f"# Welcome to the Adventure of a Lifetime - Metacritic comparison🎮")

st.markdown("""The goal of this part is to compare personal data from my videogame_lifetime database with the data from Metacritic.
            
            **Compare data from Metacritic dataset**
            
            The available Metacritic dataset dates back from 2016;
            
            Remaing data past 2016 fetched through web scraping from metacritic webpage for set of consoles I played.
            Side notebook updated the 2016 dataset used & displayed here. Only the {df_vg.size}
            
            """)
#%% import data

df_meta['game_name'].fillna('NaN', inplace=True)
# df_meta['fuzz'] = df_meta['Name'].apply(lambda x : fuzzymatch_metacritic(x, df_vg))

#with tqdm(total=df_vg.shape[1]) as pbar:
tqdm.pandas()
df_vg['fuzz'] = df_vg['game_name'].apply(lambda x : fuzzymatch_metacritic(x, df_meta['game_name']))
#    pbar.update(1)

# st.write(df_meta)
st.write(df_vg)

df_merge = pd.merge(df_vg, df_meta, how='inner', left_on='fuzz', right_on='game_name', suffixes=['', '_y'])

st.write(df_merge)

fig_scatter = px.scatter(data_frame=df_merge,
                         x='perso_score',
                         y='critic_score',
                         color='console',
                         hover_name='game_name')

st.plotly_chart(fig_scatter)