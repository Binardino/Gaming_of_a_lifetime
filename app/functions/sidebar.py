import streamlit as st
from typing import Dict, Any

class SidebarKeys:
    CONSOLE     = "filter_console"
    CONSOLE_ALL = "filter_console_all"
    HOURS       = "filter_hours"
    SCORE       = "filter_score"
    FINISHED    = "filter_finished"
    GENRE       = "filter_genre"

def render_sidebar(
        df_vg,
        console_list,
        genre_list
            ) -> Dict[str, Any]:
    """
    Declare ALL sidebar widgets in one place.
    Return sidebar values as dictionary.
    """
    with st.sidebar:
        st.header('Filters')

        #Console
        st.subheader('Console')
        select_all_console = st.checkbox('Select all consoles',
                                        value = True,
                                        key   = SiderbarKeys.CONSOLE_ALL
                                        )
        
        consoles = st.multiselect('Consoles available',
                                options=console_list,
                                default = console_list if select_all_console else [],
                                key=SidebarKeys.CONSOLE,

        )

        #played_hours
        st.subheader('Hours played')
        hours = st.slider('Hours played',
                        int(df_vg["hours_played"].min()),
                        int(df_vg["hours_played"].max()),
                        (int(df_vg["hours_played"].min()), int(df_vg["hours_played"].max())), #value
                        step=1,
                        key=SiderBars.HOURS
                        )
        
        #personal_score
        st.subheader('Personal score')
        score = st.slider('Personal score',
                        int(df_vg["perso_score"]).min(),
                        int(df_vg["perso_score"]).mmax(),
                        (int(df_vg["perso_score"].min()), int(df_vg["perso_score"].max())),
                        step=1,
                        key=SidebarKeys.SCORE,
                        )
        
        #finished
        st.subheader('Finihsed game')
        finished = st.multiselect('Finished game',
                                  options=sorted(df_vf['fiished'].unique()),
                                  default=sorted(df_vf['fiished'].unique()),
                                  key=SidebarKeys.FINISHED,
                                        )

        #genre
        st.subheader('Game Genre')
        genre = st.multiselect('Game genre',
                               options=genre_list,
                               default=genre_list,
                               key=SidebarKeys.GENRE)         
                                            
    return {
        "console": sidebar_console,
        "hours": sidebar_hours,
        "score": sidebar_perso_score,
        "finish": sidebar_finish,
        "genre": sidebar_gametype
    }