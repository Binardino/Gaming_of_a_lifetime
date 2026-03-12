# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 2023

@author: langl

script for SQL connection
"""

#%%importing libraries
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

#%%%
def get_data_csv(path):
    return pd.read_csv(path)

def get_data_sql(sql, engine):
    """Low-level SQL query helper. Prefer the cached load_* functions for Streamlit pages."""
    return pd.read_sql(sql=sql, con=engine)

#%%functions
@st.cache_resource
def sql_connection():
    """
    Create and return the SQLAlchemy engine.
    @st.cache_resource: the engine is created once and shared across re-runs (connection pool).
    Never print the connection string — it contains credentials.
    """
    driver   = os.environ.get("POSTGRES_DRIVER")
    user     = os.environ.get("POSTGRES_USER")
    password = os.environ.get("POSTGRES_PASSWORD")
    database = os.environ.get("POSTGRES_DB")
    host     = os.environ.get("POSTGRES_HOST")
    port     = os.environ.get("POSTGRES_PORT")

    connection_string = f'{driver}//{user}:{password}@{host}:{port}/{database}'
    engine = create_engine(connection_string)

    return engine

@st.cache_data
def load_table(table_name: str) -> pd.DataFrame:
    """
    Load a full table from PostgreSQL by name.
    @st.cache_data: each unique table_name is cached independently.
    Context manager ensures the connection is always properly closed after the query.
    Note: table_name is developer-controlled (hardcoded in pages), not user input.
    """
    engine = sql_connection()
    query = sqlalchemy.text(f'SELECT * FROM {table_name}')
    with engine.connect() as conn:
        return pd.read_sql(sql=query, con=conn)