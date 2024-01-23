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
# adding Folder_2 to the system path
sys.path.append("..")
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
from functions.data_wrangling import *
from functions.metacritic_wrangling import *
from functions.visualisation_tools import *
from functions.db_connection import *
from tqdm import tqdm
from sklearn.preprocessing import LabelEncoder
#from pandarallel import pandarallel

# Initialization
#pandarallel.initialize(progress_bar=True)

print("local path", os.getcwd())
st.write("local path", os.getcwd())

df_vg = pd.read_csv('../../db_data/csv/df_vg_local_csv.csv')
df_meta_2016 = pd.read_csv(r'../../\db_data\csv\metacritic_6900_games_22_Dec_2016_updated.csv')
df_meta_ps4 = pd.read_csv(r'../../\db_data\csv\meta_scraper_ps4.csv')
df_meta_ps5 = pd.read_csv(r'../../\db_data\csv\meta_scraper_ps5.csv')
df_meta_switch = pd.read_csv(r'../../\db_data\csv\meta_scraper_switch.csv')
#%%data wrangling
col_mapper = { 
               'Name'           :'game_title', 
               'Platform'       :'game_platform',
               'Year_of_Release':'game_release_date', 
               'Critic_Score'   :'metascore',
               'User_Score'     :'user _score'
               }
df_meta_2016.rename(columns=col_mapper, inplace=True)               

df_meta = pd.concat([df_meta_2016, df_meta_ps4,df_meta_ps5, df_meta_switch])
   
console_mapper = { 
               'PlayStation 4'  :'PS4', 
               'PlayStation 5'  :'PS5'
               }

df_meta['game_platform'].replace(console_mapper, inplace=True)

#%% import data
df_meta['game_title'].fillna('NaN', inplace=True)
# df_meta['fuzz'] = df_meta['Name'].apply(lambda x : fuzzymatch_metacritic(x, df_vg))

#data wrangling
df_vg['console'] = df_vg['console'].str.split('|',expand=True)[0]
df_vg['console'].replace({'PS1':'PS'}, inplace=True)

tqdm.pandas()
#df_users.groupby(['userID', 'requestDate']).progress_apply(feature_rollup)
df_vg['fuzz'] = df_vg['game_name'].progress_apply(lambda x : fuzzymatch_metacritic(x, df_meta['game_title']))

# st.write(df_meta)
#%%
df_merge = pd.merge(df_vg, df_meta, how='inner', left_on=['fuzz', 'console'], right_on=['game_title', 'game_platform'])

df_merge_test = pd.merge(df_vg, df_meta, how='left', left_on=['fuzz', 'console'], right_on=['game_title', 'game_platform'], indicator=True)
#%%
#Numerica encoding of categories
label_encoder = LabelEncoder()
df_merge['game_type_encoded'] = df_merge['game_type'].astype('category').cat.codes
df_merge['console_encoded'] = df_merge['console'].astype('category').cat.codes
df_merge['game_type_label_encoder'] = label_encoder.fit_transform(df_merge['game_type'])

df_merge['score_diff'] = df_merge['metascore'] - df_merge['perso_score']

df_merge.to_csv('metacritic_merged_local.csv',index=False)
#%%
sns.pairplot(df_merge)

#%%
fig_diverging_bar = px.bar(df_merge, x='game_name', y='score_diff', color='score_diff', title='Diverging Bar Chart of Score Differences')
fig_diverging_bar.show()
#%%
import plotly.io as pio
pio.renderers.default='browser'
fig_violin = px.violin(df_merge,
                       x='game_type',
                       y='score_diff')
#                       box=True)

fig_violin.show()

fig_name_violin = px.violin(df_merge,
                       x='game_name',
                       y='score_diff')
#                       box=True)

fig_name_violin.show()


fig_strip_swarm = px.strip(df_merge, 
                           x='game_type', y='score_diff', 
                           color='game_type', 
                           title='Strip Plot with Swarm Plot by Game Type', 
                           width=800)
fig_strip_swarm.show()

fig_bar_error = px.bar(df_merge.groupby('game_type')['score_diff'].mean().reset_index(), 
                       x='game_type', y='score_diff', 
                       error_y=df_merge.groupby('game_type')['score_diff'].std().reset_index()['score_diff'], 
                       title='Mean Score Difference with Error Bars by Game Type')
fig_bar_error.show()
#%%
st.write("label encoder")
st.write(df_merge['game_type'])

df_merge_lite = df_merge[['game_name','game_type','perso_score']].copy()

corr_matrix = df_merge_lite.corr()

fig_heatmap = px.imshow(df_merge_lite,
#                        labels=dict(x='game_type', y='perso_score'),
                        x='game_type',
                        y='perso_score',
                        text_auto=True)
#df_merge.to_csv('meta_merge.csv')

df_merge.head(20)
#%%
import seaborn as sns
import matplotlib.pyplot as plt

correlation_matrix = df_merge.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()



df_vg_lite = df_vg[['game_name','fuzz']]
