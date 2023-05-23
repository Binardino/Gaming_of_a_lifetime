# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 17:53:53 2023

@author: langl
"""
# import custom_functions as cf

# #%%reading data

# df_vg = pd.read_csv('df_lifetime_gaming.csv')

# #%%data wranging
# df_vg = cf.str_cleaning(df_vg)

# #adding console brand
# #calling add console function to add console brand label depending on console names
# df_consoles = cf.add_console_tag(df_vg)

# #%% Visualisation block
# ### creating dict for general visualization settings 
# # sns.set_style(style='GnBu_d')
# sns.set(style = 'whitegrid', palette='deep', rc = {'figure.figsize':(20,10)}) 
# #figsize is not a param for sns.set BUT using rc & a dict, possible to add new params

# #%%**Treemap for each console amount of game played**

# # Using PyPlot dynamic Treemap to map, for each console and related brand, how many games have been played on each platform
# # (Encompassed PNG static image below, but availabe dynamic PyPlot chart version on [linked Google Colab]().
# # Below 2 PyPlot version : 
# # - the Dynamic version (for online usage) with Hover effect - displaying information when hovering over the chart
# # - Static version with always on information (adding specific params) - version saved as PNG for local displaying

# # plt.figure(figsize=(20,10))
# px_treemap_graph(df=df_consoles,
#                  ['brand', 'console'],
#                  agg_func='count',
#                  colour='brand',
#                  colour_dic={'PlayStation' : '#0D0BDE', 'Microsoft' :'#008D00', 'Nintendo': '#C90104' , 
#                                      'Sega':'#d787ff', 'Android':'#3DDC84'},
#                  title='Amount of game played per consoles - organized per console brand',
#                  width=1000, height=750
#                  )

# #%% squarify treemap for plotting game type
# sq_treemap_graph(df_size=dfga.values,
#                  df_value=dfga.values,
#                  label=dfga.index,
#                  colour=plt.cm.Dark2(np.random.rand(len(dfga.values))),
#                  title='Treemap version - Amount of game types played - all consoles combined'
#                  image_path='../Plots_Charts_PNG/treemap_game_type.png'
#                  )

# #%% **Distplot to measure the distribution of hours played by game**
# # 
# # I consider a game to be a good one whenever I spend more than 15-20 hours on it.
# # Especially when I pay full price for a game, I expect it to be at least 30-40 hours long, if not I consider it a scam.
# # 
# # Below distplot illustrates I spent in general between 15 & 30 for most of the games I played

# # In[49]:


# ax = sns.distplot(df_vg['hours_played'], bins=50)

# plt.title('Distribution of hours played per game', fontsize=15)
# ax.xaxis.set_major_locator(ticker.MultipleLocator(15)) #setting xticks to 15

# plt.savefig(('../Plots_Charts_PNG/distplot_hours_played_all_game.png'))
# plt.show()
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to the Gaming - Adventure of a Lifetime 🎮")

st.sidebar.success("Select a page above.")

st.markdown(
    """ Presentation to be done WIP
""")

path = 'pages/'