import streamlit as st
from typing import Dict

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
                      
                      )
    
    (label, #label 

                                  step) #step