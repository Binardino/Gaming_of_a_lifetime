#!/usr/bin/env python
# coding: utf-8

# # Goal of this notebook

# I created a list of all videogames I played over the year (cf. SQL database creation in the repo).
# 
# This notebook aims at creating data visualization over that dataset to illustrate key trends in this lifetime of gaming

# #### Importing Libraries
import sys
get_ipython().system('{sys.executable} -m pip install squarify')
get_ipython().system('{sys.executable} -m pip install pygal')
get_ipython().system('{sys.executable} -m pip freeze > requirements.txt')


#%% import blocks

from sqlalchemy import create_engine
import pymysql
import pandas as pd
import numpy as np

import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import squarify
import pygal
import plotly.express as px
import os
from dotenv import load_dotenv
load_dotenv()

# Set it None to display all rows in the dataframe
# pd.set_option('display.max_rows', 100)
pd.options.display.max_rows = 999

#%% **Connecting to local SQL database**

driver   = os.environ.get("driver")
user     = os.environ.get("user")
password = os.environ.get("password")
database = os.environ.get("database")
ip       = os.environ.get("ip")


connection_string = f'{driver}//{user}:{password}@{ip}/{database}'
print(connection_string)
engine = create_engine(connection_string)

#%%fetching SQL data
pd.read_sql('SHOW TABLES;', engine)

df_vg = pd.read_sql('SELECT * FROM my_videogames', engine, index_col='id')

df_vg = df_vg.reset_index(drop=True)

df_vg.shape

#%% Basic EDA
df_vg.head(20)


df_vg.tail(20)


df_vg.sort_values(by='perso_score')


df_vg.describe()

#exporting to CSV to save local copy of DB to work remotely
df_vg.to_csv('df_lifetime_gaming.csv', index=False)


#%%
#importing for cloud usage
df_vg = pd.read_csv('df_lifetime_gaming.csv')

#%% Data Wrangling

#There are several platforms & game_type concatenated in one cell - erasing blank for future counting
df_vg['game_type'] = df_vg['game_type'].str.replace(' | ', '')

df_vg['console'] = df_vg['console'].str.replace(' | ', '')

df_vg.head(20)


#%% **Counting most played console type**

# several game types in one cell
# split over '|' character & value counts
pd.Series(df_vg['console'].str.split(pat='|').sum()).value_counts()


# **Creating new sub df focusing on console**

# Sub df to measure amount of game played on each console - for later on visualization
df_consoles =  pd.DataFrame(pd.Series(df_vg['console'].str.split(pat='|').sum()).value_counts())

df_consoles.reset_index(inplace=True)

df_consoles.columns = ['console', 'count']

df_consoles

#%%**Adding Brand column for each console**

# Original dataset just has info over the console used
# adding extra info regarding the Brand of each console, to do custom visualization later on

condlist = [df_consoles['console'].str.startswith('PS'),df_consoles['console'].str.startswith('PC'),
            df_consoles['console'].str.startswith('Mega'), df_consoles['console'].str.startswith('Android')]
choicelist = ['PlayStation', 'Microsoft', 'Sega', 'Android']
df_consoles['brand'] = np.select(condlist, choicelist, default='Nintendo')

df_consoles

#%% **Counting most played game type**

# several game types in one cell
# split over '|' character & value counts
pd.Series(df_vg['game_type'].str.split(pat='|').sum()).value_counts()


# ### Data visualization

# Starting with classical Seaborn pairplot to measure potential correlation :
# - raw pairplot
# - pairplot with hue on 'finished' games

sns.pairplot(df_vg)

sns.pairplot(df_vg, hue='finished')


#%% **Treemap for each console amount of game played**

# Using PyPlot dynamic Treemap to map, for each console and related brand, how many games have been played on each platform
# (Encompassed PNG static image below, but availabe dynamic PyPlot chart version on [linked Google Colab]().
# Below 2 PyPlot version : 
# - the Dynamic version (for online usage) with Hover effect - displaying information when hovering over the chart
# - Static version with always on information (adding specific params) - version saved as PNG for local displaying

fig_console = px.treemap(data_frame=df_consoles, 
                         path=['brand', 'console'], 
                         values='count', 
                         color='brand',
                         color_discrete_map={'PlayStation' : '#0D0BDE', 'Microsoft' :'#008D00', 'Nintendo': '#C90104' , 
                                             'Sega':'#d787ff', 'Android':'#3DDC84'},
                         title='Amount of game played per consoles - organized per console brand',
                         width=1000, height=750
                        )
# fig_console.write_image('../Plots_Charts_PNG/console_distribution.png')
fig_console.show()


# plt.figure(figsize=(20,10))
fig_console = px.treemap(data_frame=df_consoles, 
                         path=['brand', 'console'], 
                         values='count', 
                         color='brand',
                         color_discrete_map={'PlayStation' : '#0D0BDE', 'Microsoft' :'#008D00', 'Nintendo': '#C90104' , 
                                             'Sega':'#d787ff', 'Android':'#3DDC84'},
                         title='Amount of game played per consoles - organized per console brand',
                         width=1000, height=750
                        )
#adding param for always displaying information for saving locally PNG image without hover effect
fig_console.data[0].textinfo = 'label+text+value'
# fig_console.layout.hovermode = False
fig_console.write_image('../Plots_Charts_PNG/console_distribution.png')
fig_console.show()


# <img src= 'https://raw.githubusercontent.com/Binardino/Gaming_of_a_lifetime/master/Plots_Charts_PNG/console_distribution.png'>

# df_vg_test.head(20)

dfga = pd.Series(df_vg['game_type'].str.split(pat='|').sum()).value_counts()
dfga
#%% ### creating dict for general visualization settings 
# sns.set_style(style='GnBu_d')
sns.set(style = 'whitegrid', palette='deep', rc = {'figure.figsize':(20,10)}) 
#figsize is not a param for sns.set BUT using rc & a dict, possible to add new params

#%% generating barchart
ax = sns.barplot(x=dfga.index, y=dfga.values, data=dfga, 
                 palette='bright',
                 order=dfga.values, orient=45, alpha=0.9)
ax.set_xticklabels(dfga.index, rotation=45)

for p in ax.patches:
             ax.annotate("%.f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='center', fontsize=11, color='black', xytext=(0, 5),
                 textcoords='offset points')
        
plt.title('Amount of game types played - all consoles combined', fontsize=15)
plt.savefig('../Plots_Charts_PNG/barplot_game_type.png')
plt.show()

#%% generating TreeMap
# plt.figure(figsize=(20,10))
squarify.plot(sizes=dfga.values, 
              value=dfga.values, 
              label=dfga.index,
#               pad = True, #to add white space between rectangles,
              color = plt.cm.Dark2(np.random.rand(len(dfga.values))),
              alpha=.8 )
plt.title('Treemap version - Amount of game types played - all consoles combined', fontsize=15)
plt.axis('off')
plt.savefig(('../Plots_Charts_PNG/treemap_game_type.png'))
plt.show()

#%% **Distplot to measure the distribution of hours played by game**
# 
# I consider a game to be a good one whenever I spend more than 15-20 hours on it.
# Especially when I pay full price for a game, I expect it to be at least 30-40 hours long, if not I consider it a scam.
# 
# Below distplot illustrates I spent in general between 15 & 30 for most of the games I played

# In[49]:


ax = sns.distplot(df_vg['hours_played'], bins=50)

plt.title('Distribution of hours played per game', fontsize=15)
ax.xaxis.set_major_locator(ticker.MultipleLocator(15)) #setting xticks to 15

plt.savefig(('../Plots_Charts_PNG/distplot_hours_played_all_game.png'))
plt.show()


#%%# **Distplot to measure how many games a year I played**
# 
# Checking below on which years have I been playing the most.
# Being born in 1987, I played the most, as a teenager & in my late 20s up untill now ;
# - during mid 1990s (on Megadrive & PC mainly) up to the mid-2000s (on PS2 & PC)
# - during my college year, I dropped down heavily on playing (just some random PC & Wii gaming sessions here & there)
# - starting mid-2010s, when I started my professional life, I got myself a PS3 & PS4 & catched up on all crazy games I haven't had a chance to play

df_vg['played_year'].hist(bins=25)
plt.title('Amount of games played per year',fontsize=15)
plt.savefig(('../Plots_Charts_PNG/distplot_hours_played_all_game.png'))
plt.show()


#%% **Distplot to measure whether I played a game right when it realises**
# 
# Checking below how much time is there between a game releases and me playing it.
# In my early years, I waited several years before playing it :
# - logically, most of early Nintendo & Sega games released in the late 80s, when I was obviously too young to buy & play them
# - except for the gap in 2008-2013 when I seldom played, from 2014 onwards, I had the tendency of playing a game closely after its release

sns.distplot(df_vg['published_year'], bins=30)
sns.distplot(df_vg['played_year'], bins=30)
plt.title('Difference between Publication Year & Year I played it')
plt.savefig(('../Plots_Charts_PNG/distplot_difference_publication.VS.played_year.png'))
plt.show()

df_dfga = pd.DataFrame(dfga).reset_index=True

df_dfga


#%%# **Scatter plot of amount of hours played per console**
# 
# Creating sub df (df_1_console) with only 1 console per row
# applying lambda function to replace 2 consoles by the 1st entry whenever there are 2

df_1_console = df_vg.copy()

df_1_console['console'] = df_1_console['console'].apply(lambda x: x.split('|')[0] if x else x)

sns.scatterplot(x='hours_played', y='perso_score', hue='console', data=df_1_console)
# plt.title()
plt.savefig(('../Plots_Charts_PNG/distplot_hours_played_all_game.png'))
plt.show()


#%%# ### Plotly scatterplot version 

fig  = px.scatter(df_1_console, x='hours_played', y='perso_score', color='console')

fig.show()

###To be Done : same scatter plot with BOKEH to make it interactive


#%%**Boxplot of score per console**
# 
# Checking for each console the spread of score of each game
# Overall, PlayStation game have the highest score mean, whereas older games from NES & Megadrive have the lowest score mean


sns.catplot(x='console', y='perso_score', kind='boxen',height=5,aspect=3, data=df_1_console)

#%%# Original dataset just has info over the console used
# adding extra info regarding the Brand of each console, to do custom visualization later on

condlist = [df_1_console['console'].str.startswith('PS'),df_1_console['console'].str.startswith('PC'),
            df_1_console['console'].str.startswith('Mega'), df_1_console['console'].str.startswith('Android')]
choicelist = ['PlayStation', 'Microsoft', 'Sega', 'Android']
df_1_console['brand'] = np.select(condlist, choicelist, default='Nintendo')

df_1_console


px.box(df_1_console ,x='console', y='perso_score', width=1000, height=400,
       color='brand', color_discrete_map={'Nintendo':'red', 'PlayStation':'blue', 'Microsoft':'green'})


sns.catplot(x='console', y='hours_played', kind='boxen',height=7,aspect=3, data=df_1_console)