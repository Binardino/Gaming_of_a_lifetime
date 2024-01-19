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
import functions.db_connection as db_co

st.set_page_config(page_title="page3 - How long to beat analysis")
#%%#%% import data
engine_vg = db_co.sql_connection()

query = sqlalchemy.text('SELECT * FROM gaming_lifetime')
print(pd.read_sql(sql=query, con=engine_vg.connect(), index_col='id'))

df_raw = get_data_sql(sql=query, engine=engine_vg.connect())

df_hltb = get_data_sql(sql=sqlalchemy.text('SELECT * FROM how_long_to_beat'), engine=engine_vg.connect())
st.write(df_hltb)
