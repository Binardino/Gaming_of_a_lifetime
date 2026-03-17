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

def _int_range(series):
    """(min, max) as ints — NaN treated as 0, empty/flat series returns sensible range."""
    clean = series.fillna(0)
    if clean.empty:
        return 0, 1
    lo, hi = int(clean.min()), int(clean.max())
    if lo == hi:
        return lo, lo + 1  # st.slider requires min < max (strict)
    return lo, hi

def _sorted_unique(series):
    """Sorted unique values, NaN excluded."""
    return sorted(series.dropna().unique())

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
        h_min, h_max = _int_range(df_vg["hours_played"])
        hours = st.slider('Hours played',
                        h_min, h_max, (h_min, h_max),
                        step=1,
                        key=SidebarKeys.HOURS
                        )

        #personal_score
        st.subheader('Personal score')
        s_min, s_max = _int_range(df_vg["perso_score"])
        score = st.slider('Personal score',
                        s_min, s_max, (s_min, s_max),
                        step=1,
                        key=SidebarKeys.SCORE,
                        )

        #finished
        st.subheader('Finished game')
        finish_opts = _sorted_unique(df_vg['finished'])
        finish = st.multiselect('Finished game',
                                  options=finish_opts,
                                  default=finish_opts,
                                  key=SidebarKeys.FINISHED,
                                        )

        #genre
        st.subheader('Game Genre')
        genre = st.multiselect('Game genre',
                               options=genre_list,
                               default=genre_list,
                               key=SidebarKeys.GENRE)

        #country_dev
        country = None
        if 'country_dev' in df_vg.columns:
            st.subheader('Developer Country')
            country_opts = _sorted_unique(df_vg['country_dev'])
            country = st.multiselect('Developer Country',
                                   options=country_opts,
                                   default=country_opts,
                                   key=SidebarKeys.COUNTRY)
        #studio
        studio = None
        if 'studio' in df_vg.columns:
            st.subheader('Studio')
            studio_opts = _sorted_unique(df_vg['studio'])
            studio = st.multiselect('Studio',
                                   options=studio_opts,
                                   default=studio_opts,
                                   key=SidebarKeys.STUDIO)
        #editor
        editor = None
        if 'editor' in df_vg.columns:
            st.subheader('Editor')
            editor_opts = _sorted_unique(df_vg['editor'])
            editor = st.multiselect('Editor',
                                   options=editor_opts,
                                   default=editor_opts,
                                   key=SidebarKeys.EDITOR)

        # Keys must match exactly what apply_filters() expects in filters.py.
        return {
        "f_console"      : console,
        "f_hours_played" : hours,
        "f_perso_score"  : score,
        "f_finish"       : finish,
        "f_genre"        : genre,
        "f_country"      : country,
        "f_studio"       : studio,
        "f_editor"       : editor
    }