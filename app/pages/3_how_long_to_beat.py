import streamlit as st
import plotly.express as px
import sys
from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
sys.path.append(str(CURRENT_FILE.parent.parent))

import functions.db_connection as db_co
from functions.data_wrangling import str_cleaning, clean_df_list
from functions.sidebar import render_sidebar
from functions.filters import apply_filters

st.set_page_config(page_title="Page 3 - How Long To Beat analysis")

#%% README
st.write(f"# Welcome to the Adventure of a Lifetime - How long to beat comparison🎮")

st.markdown(f"""The goal of this part is to compare my personal data from my videogame_lifetime database with the data from How Long To Beat (HLTB). 
            HLTB is an crowd sourced database, agregating the time the players took to finish a game. 
            
            **Compare data from HLTB dataset**
            
            The available How Long To Beat is up-to-date with data fetching ;
            
            List how long takes a game to be done at various stages. Only the {df_hltb.size}

            In How long to beat, the time the gamer took to play a game is divided in 4 categories
            - comp_100 
            - comp_all
            - comp_main
            - comp_plus

            """)
#%%
st.subheader("""Scatter plot of hour differences between personal played hours & main completional hours - by game type""")

st.write("""Scatter plot to display hour differences between personal played hours & main completional hours from HLTB - by game type""")

fig_scatter = px.scatter(data_frame=df_hltb,
                       x='hours_played',
                       y='comp_main',
                       color='game_type',
                       hover_name='game_name')
                       #box=True)
                       #kde=50)

st.plotly_chart(fig_scatter)
#%%
st.subheader("""Violin plot of score differences between personal scores & meta scores - by game name""")

st.write("""Violin plot to display for every single game name the score difference spread between my personal scores and the ones from Metacritic.""")

fig_violin = px.violin(data_frame=df_hltb,
                       x='game_name',
                       y=['hours_played', 'comp_all'],
                       box=True)
                       #kde=50)

st.plotly_chart(fig_violin)
#%%
st.subheader("""Violin plot of score differences between personal scores & meta scores - by game name""")

st.write("""Violin plot to display for every single game name the score difference spread between my personal scores and the ones from Metacritic.""")

fig_boxplot = px.box(data_frame=df_hltb,
                     x='game_name', 
                     y=['hours_played', 'comp_all'],
                     width=1000, height=400,
                     color='platform'
                     )

st.plotly_chart(fig_boxplot)

#%% violin plot
st.subheader("""Violin plot of score differences between personal scores & meta scores - by game type""")

st.write("""Violin plot to display for each game genre the score difference spread between my personal scores and the ones from Metacritic.""")

fig_violin = px.violin(df_hltb,
                       x='game_type',
                       y='plus_diff',
                       color='game_type',
                       title='Violin plot of Main + Plus hours difference per Game type',
                       box=True)

st.plotly_chart(fig_violin)
#%% Swarm plot
st.subheader("""Swarm plot of score differences between personal scores & meta scores - by game type""")

st.write("""Violin plot to display for every single game name the score difference spread between my personal scores and the ones from Metacritic.""")


fig_strip_swarm = px.strip(df_hltb, 
                           x='game_type', y='plus_diff', 
                           hover_name='game_name',
                           color='game_type', 
                           title='Strip Plot with Swarm Plot by Game Type', 
                           width=800)
st.plotly_chart(fig_strip_swarm)

#%%
st.subheader("""Violin plot of score differences between personal scores & meta scores - by game name""")

st.write("""Violin plot to display for every single game name the score difference spread between my personal scores and the ones from Metacritic.""")

fig_radar = px.line_polar(df_hltb, 
                          r='game_name', 
                          theta=['hours_played', 'comp_all'], 
                          line_close=True)

st.plotly_chart(fig_radar)