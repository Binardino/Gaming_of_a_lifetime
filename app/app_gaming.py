# -*- coding: utf-8 -*-
"""
Created on Sat May 6 16:04:01 2023

@author: Binardo Surface
"""
# Imports
import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os
#from ..script.python.functions.data_wrangling import *

#import data
@st.cache_data
def get_data_csv(path):
    return pd.read_csv(path)

@st.cache_data
def get_data_sql(query, engine):
    return pd.read_sql(query=query, con=engine)

#read df
df_vg = get_data_csv('../data/df_vg_local_csv.csv')

#display
st.title('Gaming of a lifetime df display')
st.markdown("""
Presentation of the up-to-date data from Gaming of a lifetime project""")

st.write(df_vg)

#create sliders
st.sidebar.header("select console")
console_list = df_vg.console.unique()
sidebar_console = st.sidebar.multiselect('Consoles available', console_list)

st.sidebar.header('hours played')
sidebar_hours = st.sidebar.slide('hours played', 
                                 int(df_vg.hours_played.min()),
                                  int(df_vg.hours_played.max()))