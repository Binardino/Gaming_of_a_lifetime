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
#%% README
st.set_page_config(page_title="page2 - Metacritic analysis")

st.write(f"# Welcome to the Adventure of a Lifetime - Metacritic comparison🎮")

st.markdown("""The goal of this part is to compare personal data from my videogame_lifetime database with the data from Metacritic.
            
            **Compare data from Metacritic dataset**
            
            The available Metacritic dataset dates back from 2016;
            
            Remaing data past 2016 fetched through web scraping from metacritic webpage for set of consoles I played.
            Side notebook updated the 2016 dataset used & displayed here. Only the {df_vg.size}
            
            """)

#%%#%% import data
engine_vg = db_co.sql_connection()

query = sqlalchemy.text('SELECT * FROM metacritic')
print(pd.read_sql(sql=query, con=engine_vg.connect()))
df_meta = db_co.get_data_sql(sql=query, engine=engine_vg.connect())

query = sqlalchemy.text('SELECT * FROM gaming_lifetime')
df_vg = db_co.get_data_sql(sql=query, engine=engine_vg.connect())
#st.write(df_vg)

#%% correlation between scores
st.write("""I want to establish, for both my personal scores and the one from Metacritic,
         whether there is a correlation between the scores and the type of games.""")


#Numerica encoding of categories
df_merge['game_type2'] = df_merge['game_type'].astype('category').cat.codes
df_merge['console'] = df_merge['console'].astype('category').cat.codes

st.write("label encoder")
st.write(df_merge['game_type'])

fig_heatmap = px.imshow(df_merge,
                        x='game_type',
                        y='perso_score',
                        text_auto=True)

st.plotly_chart(fig_heatmap)