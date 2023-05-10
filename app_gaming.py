# -*- coding: utf-8 -*-
#%%
"""
Created on Sat May 6 16:04:01 2023

@author: Binardo Surface
"""
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
#sys.path.insert(1, '../script/python/functions')
from script.python.functions.data_wrangling import *
#from script.python.functions.db_connection import *
from script.python.functions.visualisation_tools import *

#import data
#@st.cache_data
def get_data_csv(path):
    return pd.read_csv(path)

#st.cache_data
def get_data_sql(query, engine):
    return pd.read_sql(query=query, con=engine)
#%%
#read df
df_raw = get_data_csv('data/df_vg_local_csv.csv')

#display
st.title('Gaming of a lifetime df display')
st.markdown("""
Presentation of the up-to-date data from Gaming of a lifetime project""")

st.write(df_raw)
#%%
#str cleaning & add console tag
df_vg = str_cleaning(df_raw)

df_console_raw, console_list = clean_df_list(df_vg, 'console')

#%%
#create sliders
st.sidebar.header("select console")
sidebar_console = st.sidebar.multiselect('Consoles available', #label 
                                         console_list,
                                         console_list
                                         ) #list

st.sidebar.header('hours played')
sidebar_hours = st.sidebar.slider('hours played', #label 
                                  int(df_vg.hours_played.min()),
                                  int(df_vg.hours_played.max()),
                                  (int(df_vg.hours_played.min()), int(df_vg.hours_played.max())), #value
                                  1) #step
#%%
#creates masks from the sidebar selection widgets
mask_console = df_vg['console'].isin(sidebar_console)

#filter with hours in range of selected hours
mask_hours = df_vg['hours_played'].value_counts().between(sidebar_hours[0],
                                                          sidebar_hours[1]).to_frame()

mask_hours = df_vg['hours_played'].between(sidebar_hours[0],sidebar_hours[1])

st.write('sidebar_hours[0]', sidebar_hours[0])
st.write('sidebar_hours[1]',sidebar_hours[1])

#mask_hours = mask_hours[mask_hours['hours_played'] == 1].index.to_list()
#mask_hours = mask_hours['hours_played'].index.to_list()
st.write("mask_hours")
st.write(mask_hours)
#mask_hours = df_vg['hours_played'].isin(mask_hours)
#st.write(mask_hours)
#apply mask
subdf_filter = df_vg[mask_console & mask_hours].reset_index(drop=True)
st.markdown("""filtered df""")
st.write(subdf_filter)

#%%
#str cleaning & add console tag
df_console_raw, temp_lis = clean_df_list(subdf_filter, 'console')
df_console = add_console_tag(df_console_raw)

df_console_count = df_console.loc[df_console['console'].isin(
                                    subdf_filter['console'])].groupby(['console', 'brand']
                                            ).size().sort_values(ascending=False).reset_index(name='count')
st.markdown("""df_console_count""")
st.write(df_console_count)
#%%
#treemap console brand
st.subheader("""Treemap of amount of games per console - brand & model""")

st.caption("""Using PyPlot dynamic Treemap to map, for each console and related brand, how many games have been played on each platform
(Encompassed PNG static image below, but availabe dynamic PyPlot chart version on [linked Google Colab]().
Below 2 PyPlot version : 
- the Dynamic version (for online usage) with Hover effect - displaying information when hovering over the chart
- Static version with always on information (adding specific params) - version saved as PNG for local displaying
""")

fig_console = px.treemap(data_frame=df_console_count, 
                         path=['brand', 'console'], 
                         values='count',
                         color='brand',
                         color_discrete_map={'PlayStation' : '#0D0BDE',
                                             'Microsoft' :'#008D00',
                                             'Nintendo': '#C90104' , 
                                             'Sega':'#d787ff', 
                                             'Android':'#3DDC84'},
                         title='Amount of game played per consoles - organised per console brand',
                         width=1000, height=750
                        )

st.plotly_chart(fig_console)

#%%
#treemap game type
dfga , game_list = clean_df_list(subdf_filter, 'game_type')

dfga_count = dfga.groupby('game_type').agg({'game_type':'count'}
                                           ).rename(columns={'game_type':'count'}).reset_index()

st.subheader("""Treemap of amount of games per types""")

st.caption("""Using PyPlot Treemap to plot the amount of game played by types of games - classifcation on all consoles combined""")


fig_game = px.treemap(data_frame=dfga_count,
                      path=['game_type'],
                      values='count',
                      title='Count Games per types',
                      width=1000, height=750)

st.plotly_chart(fig_game)
#%% **Distplot to measure the distribution of hours played by game**
st.subheader("""Distplot to measure the distribution of hours played by game""")

st.caption("""I consider a game to be a good one whenever I spend more than 15-20 hours on it.
Especially when I pay full price for a game, I expect it to be at least 30-40 hours long, if not I consider it a scam.

Below distplot illustrates I spent in general between 15 & 30 for most of the games I played""")

fig_distplot = plt.figure(figsize=(13, 5))
ax = sns.distplot(df_vg['hours_played'], bins=50)

plt.title('Distribution of hours played per game', fontsize=15)
ax.xaxis.set_major_locator(ticker.MultipleLocator(15)) #setting xticks to 15

st.pyplot(fig_distplot)
#%% 
# catplot of hours played
st.subheader("""Catplot of hours played per console""")

fig_cat = plt.figure(figsize=(13, 5))
sns.catplot(x='console', y='hours_played', kind='boxen',height=7,aspect=3, data=df_vg)

st.pyplot(fig_cat)
#%% 
# catplot of hours played
st.subheader("""Distplot to measure how many games a year I played

Checking below on which years have I been playing the most. Being born in 1987, I played the most, as a teenager & in my late 20s up untill now ;

during mid 1990s (on Megadrive & PC mainly) up to the mid-2000s (on PS2 & PC)
during my college year, I dropped down heavily on playing (just some random PC & Wii gaming sessions here & there)
starting mid-2010s, when I started my professional life, I got myself a PS3 & PS4 & catched up on all crazy games I haven't had a chance to play""")

fig_dis_year = plt.figure()
df_vg['played_year'].hist(bins=25)
plt.title('Amount of games played per year',fontsize=15)

st.pyplot(fig_dis_year)

#%%
# distplot publish year
st.subheader("""Distplot to measure whether I played a game right when it realises

Checking below how much time is there between a game releases and me playing it. In my early years, I waited several years before playing it :

logically, most of early Nintendo & Sega games released in the late 80s, when I was obviously too young to buy & play them
except for the gap in 2008-2013 when I seldom played, from 2014 onwards, I had the tendency of playing a game closely after its release""")

fig_publish = plt.figure()

sns.distplot(df_vg['published_year'], bins=30)
sns.distplot(df_vg['played_year'], bins=30)
plt.title('Difference between Publication Year & Year I played it')

st.pyplot(fig_publish)

#%%
st.subheader("""Boxplot of personal scores spread per consoles
TBW
""")

#WIP add clean console 
df_vg['console'] = df_vg['console'].apply(lambda x: x.split('|')[0] if x else x)

df_vg = add_console_tag(df_vg)

fig_score_console = px.box(df_vg,
                            x='console', y='perso_score', 
                            width=1000, height=400,
                            color='brand', 
                            color_discrete_map={'Nintendo':'red', 'PlayStation':'blue', 'Microsoft':'green'}
                            )

st.plotly_chart(fig_score_console)
# %%
