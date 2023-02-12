# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 17:53:53 2023

@author: langl
"""
import custom_functions as cf

#%%reading data

df_vg = pd.read_csv('df_lifetime_gaming.csv')

#%%data wranging

#%%adding console brand
#calling add console function to add console brand label depending on console names
df_consoles = cf.add_console_tag

#%%**Treemap for each console amount of game played**

# Using PyPlot dynamic Treemap to map, for each console and related brand, how many games have been played on each platform
# (Encompassed PNG static image below, but availabe dynamic PyPlot chart version on [linked Google Colab]().
# Below 2 PyPlot version : 
# - the Dynamic version (for online usage) with Hover effect - displaying information when hovering over the chart
# - Static version with always on information (adding specific params) - version saved as PNG for local displaying

px_treemap_graph(df=df_consoles,
                 ['brand', 'console'],
                 agg_func='count',
                 colour='brand',
                 colour_dic={'PlayStation' : '#0D0BDE', 'Microsoft' :'#008D00', 'Nintendo': '#C90104' , 
                                     'Sega':'#d787ff', 'Android':'#3DDC84'},
                 title='Amount of game played per consoles - organized per console brand',
                 width=1000, height=750
                 )

px_treemap_graph( )

#%%
#ion with always on information (adding specific params) - version saved as PNG for local displaying

# plt.figure(figsize=(20,10))
fig_console = px.treemap(data_frame=df_consoles, 
                         path=['brand', 'console'], 
                         values='count', 
                         color='brand',
                         color_discrete_map={'PlayStation' : '#0D0BDE', 'Microsoft' :'#008D00', 'Nintendo': '#C90104' , 
                                             'Sega':'#d787ff', 'Android':'#3DDC84'},
                         title='Amount of game played per consoles - organized per console brand',
                         width=1000, height=750
                        )
#adding param for always displaying information for saving locally PNG image without hover effect
fig_console.data[0].textinfo = 'label+text+value'
# fig_console.layout.hovermode = False
fig_console.write_image('../Plots_Charts_PNG/console_distribution.png')
fig_console.show()