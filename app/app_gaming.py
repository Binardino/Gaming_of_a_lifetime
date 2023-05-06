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


#import data
@st.cache
def get_data_csv(path):
    return pd.read_csv(path)

@st.cache
def get_data_sql(query, engine):
    return pd.read_sql(query=query, con=engine)

#read df
df_vg = get_data_csv('../data/df_vg_local_csv.csv')

#display
st.title('Gaming of a lifetime df display')
st.markdown("""
Presentation of the up-to-date data from Gaming of a lifetime project""")

st.write(df_vg)