# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:12:45 2023

@author: langl
"""
#%%import libraries
import pandas as pd
import numpy as np

#%% define key list of unique int - required to use streamlit container items
def number_generator(number_list):
    for number in number_list:
        yield number

#%%
def str_cleaning(df):
    """cleaning str in columns to perform further analysis"""
    df['game_type']      = df['game_type'].str.replace(' / ', '', regex=False)
    df['console']        = df['console'].str.replace(' / ', '', regex=False)
    #creating console_raw column to keep raw value
    df['console_raw']    = df['console']
    #keeping one console only when several to simplify
    df['console']        = df['console'].str.split('|').explode('console').reset_index(drop=True)
    df['published_year'] = df['published_year'].astype(int)
    df['played_year']    = df['played_year'].astype(int)    
    return df

#%%
def clean_df_list(df, column):
    df_console_raw          = pd.DataFrame(df[column])
    df_console_raw[column]  = df_console_raw[column].str.split(pat='|')
    df_console_raw          = df_console_raw.explode(column).reset_index(drop=True)
    console_list            = df_console_raw[column].unique().tolist()
    
    # Create a mapping dictionary for individual values to concatenated values
    mapping_dict = {}
    for value in console_list:
        concat_values = df[df[column].str.contains(value)][column].unique().tolist()
        mapping_dict[value] = concat_values
    
    return df_console_raw, console_list, mapping_dict

#%%
def add_console_tag(df):
    """
    add console brand depending on name of console using custom condition list

    Parameters
    ----------
    df : pandas df

    Returns
    -------
    same df with new 'brand' column

    """
    condlist = [df['console'].str.startswith('PS'),
                df['console'].str.startswith('PC'),
                df['console'].str.startswith('Mega'), 
                df['console'].str.startswith('Android')]
    
    choicelist = ['PlayStation', 'Microsoft', 'Sega', 'Android']
    
    df['brand'] = np.select(condlist, 
                            choicelist, 
                            default='Nintendo')
    
    return df