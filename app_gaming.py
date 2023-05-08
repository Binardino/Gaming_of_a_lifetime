# -*- coding: utf-8 -*-
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
@st.cache_data
def get_data_csv(path):
    return pd.read_csv(path)

@st.cache_data
def get_data_sql(query, engine):
    return pd.read_sql(query=query, con=engine)

#read df
df_raw = get_data_csv('data/df_vg_local_csv.csv')

#display
st.title('Gaming of a lifetime df display')
st.markdown("""
Presentation of the up-to-date data from Gaming of a lifetime project""")

st.write(df_raw)

#str cleaning & add console tag
df_vg = str_cleaning(df_raw)

df_console_raw, console_list = create_console_list(df_vg)

#str cleaning & add console tag
df_console = add_console_tag(df_console_raw)

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

st.write(sidebar_hours)

st.write(sidebar_hours[0])
st.write(sidebar_hours[1])

#creates masks from the sidebar selection widgets
mask_console = df_vg['console'].isin(sidebar_console)

#filter with hours in range of selected hours
mask_hours = df_vg['hours_played'].value_counts().between(sidebar_hours[0],
                                                          sidebar_hours[1]).to_frame()

#mask_hours = mask_hours[mask_hours['hours_played'] == 1].index.to_list()
mask_hours = df_vg['hours_played'].isin(sidebar_console)

#apply mask
subdf_filter = df_vg[mask_console] # & mask_hours]
st.write(subdf_filter)

fig_console = px.treemap(data_frame=df_consoles, 
                         path=['brand', 'console'], 
                         values='count', 
                         color='brand',
                         color_discrete_map={'PlayStation' : '#0D0BDE', 'Microsoft' :'#008D00', 'Nintendo': '#C90104' , 
                                             'Sega':'#d787ff', 'Android':'#3DDC84'},
                         title='Amount of game played per consoles - organized per console brand',
                         width=1000, height=750
                        )

st.plotly_chart(fig_console)