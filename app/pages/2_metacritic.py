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

st.write(df_meta)

#%%data wrangling
#Numerica encoding of categories
df_meta['game_type_encoded'] = df_meta['game_type'].astype('category').cat.codes
df_meta['console_encoded']   = df_meta['console'].astype('category').cat.codes
df_meta['score_diff']        = df_meta['metascore'] - df_meta['perso_score']

#st.write(df_vg)
#generate df, console list & dictionary 
df_console_raw, console_list, dict_console = clean_df_list(df_meta, 'console')
#generate df, gametype list & dictionary
df_genre_raw, genre_list, dict_genre = clean_df_list(df_meta, 'game_type')
#%%
#create sliders
st.sidebar.header("select console")
#sidebar console text to select
sidebar_console = create_slider_multiselect(label='Consoles available', #label 
                                            column=console_list,        
                                            key=1)

st.sidebar.header('hours played')
#slider hours played to select
sidebar_hours = create_slider_numeric('hours played', df_meta.hours_played, 1)

st.sidebar.header('personal score')
#slider personal score to select
sidebar_perso_score = create_slider_numeric('perso score', df_meta.perso_score, 1)

#sidebar finish Boolean to select
#sidebar_finish = create_slider_multiselect(2,'finished game', df_meta.finished.unique())

sidebar_finish = create_slider_multiselect(label='finished game', #label 
                                            column=df_meta.finished.unique(),        
                                            key=2)

#sidebar game type text to select
#sidebar_gametype = create_slider_multiselect(3,'Game genre', #label 
                                             #genre_list)   #default     

sidebar_gametype = create_slider_multiselect(label='Game genre', #label 
                                            column=genre_list,        
                                            key=3)          
#%%
#creates masks from the sidebar selection widgets
mask_console = create_mask(df_meta, 'console', sidebar_console, dict_console)

# st.write("mask_console")
# st.write(mask_console)
#creates masks from the sidebar selection widgets
mask_gametype = create_mask(df_meta, 'game_type', sidebar_gametype, dict_genre)

#filter with hours in range of selected hours
mask_hours = df_meta['hours_played'].between(sidebar_hours[0],sidebar_hours[1])

#mask score
mask_perso_score = df_meta['perso_score'].between(sidebar_perso_score[0],sidebar_perso_score[1])

#mask finish
mask_finish = df_meta['finished'].isin(sidebar_finish)

#apply list of masks to dataset
subdf_filter = df_meta[mask_console 
                     & mask_hours 
                     & mask_finish
                     & mask_perso_score 
                     & mask_gametype
                    ].reset_index(drop=True)#& mask_perso_score

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