# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 2023

@author: langl

script for SQL connection
"""

#%%importing libraries
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()

#%%functions
def sql_connection():
    driver   = os.environ.get("driver")
    user     = os.environ.get("user")
    password = os.environ.get("password")
    database = os.environ.get("database")
    ip       = os.environ.get("ip")


    connection_string = f'{driver}//{user}:{password}@{ip}/{database}'
    print(connection_string)
    engine = create_engine(connection_string)
    
    return engine