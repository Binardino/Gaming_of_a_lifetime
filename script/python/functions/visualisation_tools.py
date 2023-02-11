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

def px_treemap_graph(df, columns, agg_func, colour, colour_mapper, title, width, height, image_path):
    """
    generate Treemap with plotly express lib
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
    -------
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

def sq_treemap_graph(df_size, df_value, label, colour, title,image_path):
    """
    generate Treemap with Squarify express lib
    Parameters
    ----------
    df_size : size of each square
    df_value : value of each square
    label : label of each square
    colour : column to use as colour code
    title : graph title
    image_path : path to save graph as PNG file

    Returns
    -------
    display & save as PNG file Plotly express Treemap graph

    """
    plt.figure(figsize=(20,10))
    squarify.plot(sizes=df_size, 
                  value=df_value, 
                  label=label,
    #               pad = True, #to add white space between rectangles,
                  color = colour,
                  alpha=.8 )
    plt.title(title, fontsize=15)
    plt.axis('off')
    plt.savefig(image_path)
    plt.show()
