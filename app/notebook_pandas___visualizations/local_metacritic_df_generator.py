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

print("local path", os.getcwd())
st.write("local path", os.getcwd())

df_vg = pd.read_csv(r'C:/test/gitio_bine/Gaming_of_a_lifetime/db_data/csv/df_vg_local_csv.csv')

df_meta_2016 = pd.read_csv(r'C:\test\gitio_bine\Gaming_of_a_lifetime\db_data\csv\metacritic_6900_games_22_Dec_2016_updated.csv')

#%% import data
df_meta['Name'].fillna('NaN', inplace=True)
# df_meta['fuzz'] = df_meta['Name'].apply(lambda x : fuzzymatch_metacritic(x, df_vg))

#data wrangling
df_vg['console'] = df_vg['console'].str.split('|',expand=True)[0]
df_vg['console'].replace({'PS1':'PS'}, inplace=True)
tqdm.pandas()
#df_users.groupby(['userID', 'requestDate']).progress_apply(feature_rollup)
df_vg['fuzz'] = df_vg['game_name'].progress_apply(lambda x : fuzzymatch_metacritic(x, df_meta['Name']))

# st.write(df_meta)

df_merge = pd.merge(df_vg, df_meta, how='inner', left_on=['fuzz', 'console'], right_on=['Name', 'Platform'])

df_merge_test = pd.merge(df_vg, df_meta, how='left', left_on=['fuzz', 'console'], right_on=['Name', 'Platform'], indicator=True)

#Numerica encoding of categories
label_encoder = LabelEncoder()
df_merge['game_type2'] = df_merge['game_type'].astype('category').cat.codes
df_merge['console'] = df_merge['console'].astype('category').cat.codes
df_merge['game_type'] = label_encoder.fit_transform(df_merge['game_type'])

st.write("label encoder")
st.write(df_merge['game_type'])

df_merge_lite = df_merge[['game_name','game_type','perso_score']].copy()

corr_matrix = df_merge_lite.corr()

fig_heatmap = px.imshow(df_merge_lite,
#                        labels=dict(x='game_type', y='perso_score'),
                        x='game_type',
                        y='perso_score')

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
