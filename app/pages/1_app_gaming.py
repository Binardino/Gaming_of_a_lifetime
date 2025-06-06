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
import sqlalchemy
#set path for dynamic function import
from pathlib import Path
# Adds the parent directory of this script to sys.path
CURRENT_FILE = Path(__file__).resolve()
PAGES_DIR = CURRENT_FILE.parent
ROOT_DIR = PAGES_DIR.parent
sys.path.append(str(ROOT_DIR))
from functions.data_wrangling import *
from functions.db_connection import *
from functions.visualisation_tools import *
from functions.sidebar_filters import *
from functions.mask_df_utils import *
import functions.db_connection as db_co
#from functions.data_wrangling import number_generator
st.set_page_config(page_title="Gaming EDA presentation")
#%%
#read df
engine = db_co.sql_connection()
query = sqlalchemy.text('SELECT * FROM gaming_lifetime')
print(pd.read_sql(sql=query, con=engine.connect(), index_col='id'))
df_raw = get_data_sql(sql=query, engine=engine.connect())
#display
st.title('Gaming of a lifetime df display')
st.markdown("""
Presentation of the up-to-date data from Gaming of a lifetime project
Update with applied filters""")
#%%
#str cleaning & add console tag
df_vg = str_cleaning(df_raw)
#generate df, console list & dictionary 
df_console_raw, console_list, dict_console = clean_df_list(df_vg, 'console')
#generate df, gametype list & dictionary
df_genre_raw, genre_list, dict_genre = clean_df_list(df_vg, 'game_type')
#%%
# Global counter to generate unique keys
key_counter = 0

def get_unique_key(prefix="chart"):
    """Generates a unique key using a global counter."""
    global key_counter
    key_counter += 1
    return f"{prefix}_{key_counter}"

#random key generator
#random_key = range(10)

#get_unique_key = number_generator(random_key)
#%%
# Inject custom CSS to set the width of the sidebar
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 300px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)
# Assume you have loaded df_vg, console_list, genre_list, dict_console, dict_genre
#subdf_filter = apply_sidebar_filters(df_vg, console_list, genre_list, dict_console, dict_genre)
#%% filters

# Set up initial session state values once
init_sidebar_state(console_list, genre_list, df_vg)

filters = create_sidebar_widgets(df_vg, console_list, genre_list)

subdf_filter = apply_all_masks(df_vg, filters, dict_console=dict_console, dict_genre=dict_genre)

st.markdown("""filtered df""")
st.dataframe(subdf_filter)
#%%
#str cleaning & add console tag
#df_console_raw, temp_lis, dict_console_temp = clean_df_list(subdf_filter, 'console')
df_console = add_console_tag(df_console_raw)

df_console_count = df_console.loc[df_console['console'].isin(
                                    subdf_filter['console'])].groupby(['console', 'brand']
                                            ).size().sort_values(ascending=False).reset_index(name='count')

st.write("df_console_count")
st.dataframe(df_console_count)
#%%
#treemap console brand
st.subheader("""Treemap of amount of games per console - brand & model""")

st.caption("""Using PyPlot dynamic Treemap to map, for each console and related brand, how many games have been played on each platform
Hover effect - displaying information when hovering over the chart""")

fig_console = px.treemap(data_frame=df_console_count, 
                         path=['brand', 'console'], 
                         values='count',
                         color='brand',
                         color_discrete_map={'PlayStation' : '#0D0BDE',
                                             'Microsoft'   : '#008D00',
                                             'Nintendo'    : '#C90104' , 
                                             'Sega'        : '#d787ff', 
                                             'Android'     : '#3DDC84'},
                         title='Treemap graph - Amount of game played per consoles - organised per console brand',
                         width=1000, height=750
                        )

st.plotly_chart(fig_console)
#%%
#add Sunburst diagram for games per console
st.subheader("""Sunburst of amount of games per console - brand & model""")
st.caption("""Similar chart with Sunburst viz""")

fig_sunburst = px.sunburst(data_frame=df_console_count,
                       path=['brand', 'console'], 
                         values='count',
                         color='brand',
                         color_discrete_map={'PlayStation' : '#0D0BDE',
                                             'Microsoft'   : '#008D00',
                                             'Nintendo'    : '#C90104' , 
                                             'Sega'        : '#d787ff', 
                                             'Android'     : '#3DDC84'},
                         title='Sunburst graph - Amount of game played per consoles - organised per console brand',
                         width=1000, height=750)

st.plotly_chart(fig_sunburst)
#%%
#treemap game type
dfga , game_list, game_list_temp = clean_df_list(subdf_filter, 'game_type')

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

selection_hours = st.selectbox('select viz library', ['plotly', 'seaborn'],key=get_unique_key())
if selection_hours == 'seaborn':
    fig_distplot = plt.figure(figsize=(13, 5))
    ax = sns.histplot(subdf_filter['hours_played'], 
                      kde=True , 
                      bins=50)

    plt.title('Distribution of hours played per game', fontsize=15)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(15)) #setting xticks to 15

    st.pyplot(fig_distplot)

elif selection_hours == 'plotly':
    fig_px_histo_hours = px.histogram(subdf_filter, x="hours_played",# y="hours_played", #color="sex",
                                      marginal="box", nbins=90,# or violin, rug
                                      hover_data=subdf_filter.columns)
    st.plotly_chart(fig_px_histo_hours)
#%% 
# catplot of hours played
st.subheader("""Catplot of hours played per console""")

fig_cat = plt.figure(figsize=(13, 5))
sns.boxenplot(x='console', y='hours_played', data=subdf_filter)

st.pyplot(fig_cat)
#%% 
# catplot of hours played
st.subheader("""Distplot to measure how many games a year I played

Checking below on which years have I been playing the most. Being born in 1987, I played the most, as a teenager & in my late 20s up untill now ;

during mid 1990s (on Megadrive & PC mainly) up to the mid-2000s (on PS2 & PC)
during my college year, I dropped down heavily on playing (just some random PC & Wii gaming sessions here & there)
starting mid-2010s, when I started my professional life, I got myself a PS3 & PS4 & catched up on all crazy games I haven't had a chance to play""")

selection_dist_year = st.selectbox('select viz library', ['plotly', 'seaborn'],key=get_unique_key())
if selection_dist_year == 'seaborn':
    fig_dis_year = plt.figure()
    subdf_filter['played_year'].hist(bins=25)
    plt.title('Amount of games played per year',fontsize=15)

    st.pyplot(fig_dis_year)

elif selection_dist_year == 'plotly':
    fig_px_histo_years = px.histogram(subdf_filter, x="played_year",# y="hours_played", #color="sex",
                                      marginal="box",
                                      color='console', 
                                      nbins=90,# or violin, rug
                                      hover_data=subdf_filter.columns)
    
    st.plotly_chart(fig_px_histo_years)
#%%area chart
def get_df_long_format(df, column_list,year_column,agg_column,renamed_column):
    df_temp_year = df.groupby([column_list]).agg({agg_column : 'count'}) \
                                           .rename(columns={agg_column: f"{agg_column}_count"}) \
                                           .reset_index()

    df_year_pivot = pd.pivot(data=df_temp_year,
                             index=year_column,
                             columns=agg_column,
                             values=f"{agg_column}_count"
                             )
    
    df_year_pct = df_year_pivot.fillna(0).div(df_year_pivot.sum(axis=1), axis=0)

    return df_year_pct

df_console_year = subdf_filter.groupby(['played_year', 'console']).agg({'console'  : 'count'}) \
                                                                    .rename(columns={'console':'console_count'}) \
                                                                    .reset_index()    
df_console_year_pivot = pd.pivot(data=df_console_year,
                            index='played_year',
                            columns='console',
                            values='console_count')

df_console_year_pct = df_console_year_pivot.fillna(0).div(df_console_year_pivot.sum(axis=1), axis=0)

#df2 = df_long_filled.div(df_long_filled.sum(axis=1), axis=0)
#st.write(df2)
#for col in df_console_year2.columns:
#    df_console_year2[col] = df_console_year2[col].fillna(0).div(df_console_year2[col].sum(axis=1), axis=0).multiply(100)

# Assuming df is your DataFrame
fig = px.area(data_frame=df_console_year_pct, 
              x=df_console_year_pct.index,  y=df_console_year_pct.columns[1:], #facet_col='played_year',
              title='Stack Area Chart of Games Played by Console Over the Years',
              labels={'console_count': 'Percentage of Games Played', 'year': 'Year'},
              category_orders={'played_year': sorted(df_console_year['played_year'].unique())},
              #height=600, facet_col_wrap=3, facet_col_spacing=0.05
              )

fig.update_layout(xaxis=dict(type='category'), yaxis=dict(title='Percentage'))

#st.write)
st.plotly_chart(fig, key=get_unique_key())

#%%
# distplot publish year
st.subheader("""Distplot to measure whether I played a game right when it got released

Checking below how much time is there between a game release and me playing it. In my early years, I waited several years before playing it :

logically, most of early Nintendo & Sega games released in the late 80s, when I was obviously too young to buy & play them
except for the gap in 2008-2013 when I seldom played, from 2014 onwards, I had the tendency of playing a game closely after its release""")

selection_pub_year = st.selectbox('select viz library', ['plotly', 'seaborn'],key=get_unique_key())
if selection_pub_year == 'seaborn':
    fig_publish = plt.figure(figsize=(10,6))

    sns.histplot(subdf_filter['published_year'], 
                kde=True , 
                bins=30, 
                color=[0,.5,0],
                label='published_year')

    sns.histplot(subdf_filter['played_year'], 
                kde=True,
                bins=30,  
                color=[0,0,1],
                label='played_year')

    plt.xlabel('Years')
    plt.legend(loc=2) #upper left
    plt.title('Difference between Publication Year & Year I played it')

    st.pyplot(fig_publish)

elif selection_pub_year == 'plotly':
    df_test_year = subdf_filter[['published_year','played_year']].copy()
    fig_px_publish = px.histogram(subdf_filter.loc[(subdf_filter['published_year'].notna()) & (subdf_filter['played_year'].notna())], x=["published_year", 'played_year'],
                                      opacity=0.5, marginal="box", nbins=90, barmode='overlay')
    

    st.plotly_chart(fig_px_publish)
#%%
st.subheader("""Boxplot of personal scores spread per consoles
TBW
""")

#WIP add clean console 
subdf_filter['console'] = subdf_filter['console'].apply(lambda x: x.split('|')[0] if x else x)

df_vg = add_console_tag(subdf_filter)

selection_score_console = st.selectbox('select viz library', ['plotly', 'seaborn'],key=get_unique_key())

if selection_score_console == 'plotly':
    fig_score_console = px.box(df_vg,
                                x='console', y='perso_score', 
                                width=1000, height=400,
                                color='brand', 
                                color_discrete_map={'Nintendo':'red', 'PlayStation':'blue', 'Microsoft':'green'}
                                )

    st.plotly_chart(fig_score_console)
# %%
#WIP add clean console 
st.subheader("""Scatterplot of played hours per personal scores
TBW
""")
selection_scatterscore = st.selectbox('select viz library', ['plotly', 'seaborn'],key=get_unique_key())

if selection_scatterscore == 'plotly':
    fig_scatterscore = px.scatter(subdf_filter, 
                                x='hours_played', y='perso_score', 
                                color='console',
                                hover_name='game_name')

    st.plotly_chart(fig_scatterscore)

if selection_scatterscore == 'seaborn':
    fig_scatter = plt.figure(figsize=(13, 5))
    
    sns.scatterplot(x='hours_played', y='perso_score', hue='console', data=subdf_filter)
# plt.title()
    st.pyplot(fig_scatter)

#%%
st.subheader("""Boxplot of score per console

Checking for each console the spread of score of each game Overall, PlayStation game have the highest score mean, whereas older games from NES & Megadrive have the lowest score mean
TBW
""")
fig_boxscore = plt.figure(figsize=(13, 5))
sns.boxenplot(data=subdf_filter, x='console', y='perso_score')
sns.stripplot(data=subdf_filter, x='console', y='perso_score')

st.pyplot(fig_boxscore)
#%% TBD
df_type_year_raw = subdf_filter.copy()
st.write("df_type_year_raw")
st.dataframe(df_type_year_raw)
df_type_year = df_type_year_raw.groupby(['played_year', 'game_type']).agg({'game_type': 'count'}) \
                                                                    .rename(columns={'game_type':'type_count'}) \
                                                                    .reset_index()

df_console_year = df_type_year_raw.groupby(['played_year', 'console']).agg({'console'  : 'count'}) \
                                                                    .rename(columns={'console':'console_count'}) \
                                                                    .reset_index()

st.subheader("""Stack Area Chart of Games Played by Console Over the Years""")

st.caption("""I consider a game to be a good one whenever I spend more than 15-20 hours on it.
Especially when I pay full price for a game, I expect it to be at least 30-40 hours long, if not I consider it a scam.

Below distplot illustrates I spent in general between 15 & 30 for most of the games I played""")
# Assuming df is your DataFrame
fig2 = px.area(data_frame=df_console_year_pct, 
              x=df_console_year_pct.index,  y=df_console_year_pct.columns[1:], #facet_col='played_year',
              title='Stack Area Chart of Games Played by Console Over the Years',
              labels={'console_count': 'Percentage of Games Played', 'year': 'Year'},
              category_orders={'played_year': sorted(df_console_year['played_year'].unique())},
              #height=600, facet_col_wrap=3, facet_col_spacing=0.05
              )

fig2.update_layout(xaxis=dict(type='category'), yaxis=dict(title='Percentage'))

st.plotly_chart(fig2, key=get_unique_key())