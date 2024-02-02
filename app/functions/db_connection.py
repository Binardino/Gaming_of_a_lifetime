# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 2023

@author: langl

script for SQL connection
"""

#%%importing libraries
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()
#%%%
def get_data_csv(path):
    return pd.read_csv(path)

#st.cache_data
def get_data_sql(sql, engine):
    return pd.read_sql(sql=sql, con=engine)
#%%functions
def sql_connection():
    driver   = os.environ.get("POSTGRES_DRIVER")
    user     = os.environ.get("POSTGRES_USER")
    password = os.environ.get("POSTGRES_PASSWORD")
    table    = os.environ.get("POSTGRES_TABLE")
    database = os.environ.get("POSTGRES_DB")
    host     = os.environ.get("POSTGRES_HOST")
    port     = os.environ.get("POSTGRES_PORT")

    connection_string = f'{driver}//{user}:{password}@{host}:{port}/{database}'
    print(connection_string)
    engine = create_engine(connection_string)
    
    return engine