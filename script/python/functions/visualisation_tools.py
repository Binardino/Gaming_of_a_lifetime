# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 17:34:13 2023

@author: langl

list of visualisations functions
"""

#%% import libraries
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import squarify
import pygal
import plotly.express as px

#%%functions

def treemap_graph(df, columns, agg_func, colour, colour_mapper, title, width, height, image_path):
    """
    Parameters
    ----------
    df : dataframe TYPE pandas df
    columns : list of columns to use for graph
    agg_func : aggregation function to use
    colour : column to use as colour code
    colour_mapper : dictionary of colour to use
    title : graph title
    width : width of graph
    height : height of graph
    image_path : path to save graph as PNG file

    Returns 
    display & save as PNG file Plotly express Treemap graph
    
    """
    fig_console = px.treemap(data_frame=df, 
                             path=columns, 
                             values=agg_func, 
                             color=colour,
                             color_discrete_map=colour_mapper,
                             title=title,
                             width=width, height=height
                            )
    fig_console.write_image(image_path)
    fig_console.show()
