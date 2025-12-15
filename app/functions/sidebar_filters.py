import streamlit as st
from functions.visualisation_tools import create_slider_multiselect, create_slider_numeric, create_mask

#%%
def create_sidebar_widgets(df_vg, console_list, genre_list):
    st.sidebar.header("select console")
    sidebar_console = create_slider_multiselect(
        label='Consoles available',
        column=console_list,
        key="filter_console"
    )

    st.sidebar.header("hours played")
    sidebar_hours = create_slider_numeric(
        label='hours played',
        column=df_vg["hours_played"],
        step=1,
        key="filter_hours"
    )

    st.sidebar.header("personal score")
    sidebar_perso_score = create_slider_numeric(
        label='perso score',
        column=df_vg["perso_score"],
        step=1,
        key="filter_score"
    )

    sidebar_finish = create_slider_multiselect(
        label='finished game',
        column=df_vg["finished"].unique(),
        key="filter_finished"
    )

    st.sidebar.header('Game genre')
    sidebar_gametype = create_slider_multiselect(
        label='Game genre',
        column=genre_list,
        key="filter_genre"
    )

    return {
        "console": sidebar_console,
        "hours": sidebar_hours,
        "score": sidebar_perso_score,
        "finish": sidebar_finish,
        "genre": sidebar_gametype
    }
