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
from .script.python.functions.data_wrangling import *
from .script.python.functions.metacritic import *
from .script.python.functions.visualisation_tools import *

#%% import data
#@st.cache_data
def get_data_csv(path):
    return pd.read_csv(path)

#st.cache_data
def get_data_sql(query, engine):
    return pd.read_sql(query=query, con=engine)

df_vg = get_data_csv('./db_data/df_vg_local_csv.csv')

df_meta = get_data_csv('./db_data/metacritic_6900_games_22_Dec_2016_updated.csv')

df_meta['fuzz'] = fuzzymatch_metacritic(df_vg['game_name'])

