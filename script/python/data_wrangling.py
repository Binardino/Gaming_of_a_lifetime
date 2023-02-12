# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:12:45 2023

@author: langl
"""
#%%import libraries
import pandas as pd
import numpy as np

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