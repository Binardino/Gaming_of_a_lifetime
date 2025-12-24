import streamlit as st
from typing import Dict, Any

class SidebarKeys:
    CONSOLE     = "filter_console"
    CONSOLE_ALL = "filter_console_all"
    HOURS       = "filter_hours"
    SCORE       = "filter_score"
    FINISHED    = "filter_finished"
    GENRE       = "filter_genre"
    COUNTRY     = "filter_country"
    STUDIO      = "filter_studio"
    EDITOR      = "filter_editor"

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
                                        key   = SidebarKeys.CONSOLE_ALL
                                        )
        
        console = st.multiselect('Consoles available',
                                options = console_list,
                                default = console_list if select_all_console else [],
                                key     = SidebarKeys.CONSOLE,

        )

        #played_hours
        st.subheader('Hours played')
        hours = st.slider('Hours played',
                        int(df_vg["hours_played"].min()),
                        int(df_vg["hours_played"].max()),
                        (int(df_vg["hours_played"].min()), int(df_vg["hours_played"].max())), #value
                        step=1,
                        key=SidebarKeys.HOURS
                        )
        
        #personal_score
        st.subheader('Personal score')
        score = st.slider('Personal score',
                        int(df_vg["perso_score"].min()),
                        int(df_vg["perso_score"].max()),
                        (int(df_vg["perso_score"].min()), int(df_vg["perso_score"].max())),
                        step=1,
                        key=SidebarKeys.SCORE,
                        )
        
        #finished
        st.subheader('Finihsed game')
        finish = st.multiselect('Finished game',
                                  options=sorted(df_vg['finished'].unique()),
                                  default=sorted(df_vg['finished'].unique()),
                                  key=SidebarKeys.FINISHED,
                                        )

        #genre
        st.subheader('Game Genre')
        genre = st.multiselect('Game genre',
                               options=genre_list,
                               default=genre_list,
                               key=SidebarKeys.GENRE)         

        #country_dev
        st.subheader('Developer Country')
        country = st.multiselect('Developer Country',
                               options=sorted(df_vg['country_dev'].unique()),
                               default=sorted(df_vg['country_dev'].unique()),
                               key=SidebarKeys.COUNTRY)         
        #studio
        st.subheader('Studio')
        studio = st.multiselect('Studio',
                               options=sorted(df_vg['studio'].unique()),
                               default=sorted(df_vg['studio'].unique()),
                               key=SidebarKeys.STUDIO)         
        #editor
        st.subheader('Editor')
        editor = st.multiselect('Editor',
                               options=sorted(df_vg['editor'].unique()),
                               default=sorted(df_vg['editor'].unique()),
                               key=SidebarKeys.EDITOR)         
        
        return {
        "f_console"  : console,
        "f_hours"    : hours,
        "f_score"    : score,
        "f_finish"   : finish,
        "f_genre"    : genre,
        "f_country"  : country,
        "f_studio"   : studio,
        "f_editor"   : editor                        
    }