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
from functions.data_wrangling import *
from functions.db_connection import *
from functions.visualisation_tools import *
from functions.sidebar_filters import *
from functions.mask_df_utils import *
import functions.db_connection as db_co
#from tqdm import tqdm
#set path for dynamic function import
from pathlib import Path
# Adds the parent directory of this script to sys.path
CURRENT_FILE = Path(__file__).resolve()
PAGES_DIR = CURRENT_FILE.parent
ROOT_DIR = PAGES_DIR.parent
sys.path.append(str(ROOT_DIR))
#%%#%% import data
engine = db_co.sql_connection()
query = sqlalchemy.text('SELECT * FROM public.metacritic_merged')
print(pd.read_sql(sql=query, con=engine.connect()))
df_meta = db_co.get_data_sql(sql=query, engine=engine.connect())

query = sqlalchemy.text('SELECT * FROM gaming_lifetime')
df_vg = db_co.get_data_sql(sql=query, engine=engine.connect())
#%% README
st.set_page_config(page_title="page2 - Metacritic analysis")

st.write(f"# Welcome to the Adventure of a Lifetime - Metacritic comparison🎮")

st.markdown("# To start using the app, please select the desired filters in the filter plane")

st.markdown(f"""The goal of this part is to compare personal data from my videogame_lifetime database with the data from Metacritic.
            
            **Compare data from Metacritic dataset**
            
            The available Metacritic dataset dates back from 2016;
            Remaining data post 2016 were fetched through web scraping from metacritic webpage for the set of consoles I played.
            I end up doing the comparison between 
            data from Metacritic fetched data (size : {df_meta.size}) VS. my personal gaming of the lifetime (size : {df_vg.size})
            
            """)
#%% correlation between scores
st.write("""I want to establish, for both my personal scores and the one from Metacritic,
         whether there is a correlation between the scores and the type of games.""")
#Numerica encoding of categories
df_meta['game_type_encoded'] = df_meta['game_type'].astype('category').cat.codes
df_meta['console_encoded']   = df_meta['console'].astype('category').cat.codes
df_meta['score_diff']        = df_meta['metascore'] - df_meta['perso_score']

#generate df, console list & dictionary 
df_console_raw, console_list, dict_console = clean_df_list(df_meta, 'console')
#generate df, gametype list & dictionary
df_genre_raw, genre_list, dict_genre = clean_df_list(df_meta, 'game_type')

st.write(df_meta)
#%%
# Set up initial session state values once
init_sidebar_state(console_list, genre_list, df_meta)

filters = create_sidebar_widgets(df_meta, console_list, genre_list)

subdf_filter = apply_all_masks(df_meta, filters, dict_console=dict_console, dict_genre=dict_genre)

# Assume you have loaded df_vg, console_list, genre_list, dict_console, dict_genre
#subdf_filter = apply_sidebar_filters(df_vg, console_list, genre_list, dict_console, dict_genre)

st.markdown("""filtered df""")
st.dataframe(subdf_filter)

#%% correlation between scores
st.write("""I want to establish, for both my personal scores and the one from Metacritic,
         whether there is a correlation between the scores and the type of games.""")
#%%data wrangling
#%%
df_corr = subdf_filter.select_dtypes(include='number').corr()

sns_heatmap = plt.figure(figsize=(15, 7))
sns.heatmap(df_corr, annot=True)
st.pyplot(sns_heatmap)

fig_heatmap = px.imshow(df_corr,
                        text_auto=True)

st.plotly_chart(fig_heatmap)
#%% scatter plot
st.subheader("""Scatterplot of score differences between personal scores & meta scores - by game type""")

st.write("""Scatterplot to display for each game score differences between my personal scores and the ones from Metacritic.
         Score dot are coloured by game type ; you may hover each one to display the game name""")

fig_scatter = px.scatter(subdf_filter,
                       x='perso_score',
                       y='metascore',
                       hover_name='game_name',
                       color='game_type', 
                       title='Scatter Plot comparing my Perso Score VS. Metacritic score')

st.plotly_chart(fig_scatter)

#%% violin plot
st.subheader("""Violin plot of score differences between personal scores & meta scores - by game type""")

st.write("""Violin plot to display for each game genre the score difference spread between my personal scores and the ones from Metacritic.""")

fig_violin = px.violin(subdf_filter,
                       x='game_type',
                       y='score_diff',
                       color='game_type',
                       title='Violin plot of Score difference per Game type',
                       box=True)

st.plotly_chart(fig_violin)
#%% Swarm plot
st.subheader("""Swarm plot of score differences between personal scores & meta scores - by game type""")

st.write("""Violin plot to display for every single game name the score difference spread between my personal scores and the ones from Metacritic.""")


fig_strip_swarm = px.strip(subdf_filter, 
                           x='game_type', y='score_diff', 
                           hover_name='game_name',
                           color='game_type', 
                           title='Strip Plot with Swarm Plot by Game Type', 
                           width=800)
st.plotly_chart(fig_strip_swarm)
#%% bar plot
st.subheader("""Bar plot of score differences between personal scores & meta scores - by game name""")

st.write("""Violin plot to display for every single game name the score difference spread between my personal scores and the ones from Metacritic.""")

fig_bar_error = px.bar(subdf_filter.groupby('game_type')['score_diff'].mean().reset_index(), # 
                       x='game_type', 
                       y='score_diff', 
                       error_y=subdf_filter.groupby('game_type')['score_diff'].std().reset_index()['score_diff'], 
                       title='Mean Score Difference with Error Bars by Game Type')

st.plotly_chart(fig_bar_error)
#%% violin plot
st.subheader("""Violin plot of score differences between personal scores & meta scores - by game name""")

st.write("""Violin plot to display for every single game name the score difference spread between my personal scores and the ones from Metacritic.""")

fig_name_violin = px.violin(subdf_filter,
                       x='game_name',
                       y='score_diff',
                       color='game_type')

st.plotly_chart(fig_name_violin)