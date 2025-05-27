import streamlit as st
from functions.visualisation_tools import create_slider_multiselect, create_slider_numeric, get_unique_key, create_mask
#%%
# Global counter to generate unique keys
key_counter = 0

def get_unique_key(prefix="chart"):
    """Generates a unique key using a global counter."""
    global key_counter
    key_counter += 1
    return f"{prefix}_{key_counter}" 

    
def apply_sidebar_filters(df_vg, console_list, genre_list, dict_console, dict_genre):
    # Sliders and selections
    st.sidebar.header("Select console")
    sidebar_console = create_slider_multiselect(
        label='Consoles available',
        column=console_list,
        key=get_unique_key()
    )

    st.sidebar.header('Hours played')
    sidebar_hours = create_slider_numeric(
        label='hours played',
        column=df_vg.hours_played,
        step=1
    )

    st.sidebar.header('Personal score')
    sidebar_perso_score = create_slider_numeric(
        label='perso score',
        column=df_vg.perso_score,
        step=1
    )

    sidebar_finish = create_slider_multiselect(
        label='Finished game',
        column=df_vg.finished.unique(),
        key=get_unique_key()
    )

    st.sidebar.header('Game genre')
    sidebar_gametype = create_slider_multiselect(
        label='Game genre',
        column=genre_list,
        key=get_unique_key()
    )

    # Masks
    mask_console = create_mask(df=df_vg, column='console', slider=sidebar_console, mapping_dict=dict_console)
    mask_gametype = create_mask(df=df_vg, column='game_type', slider=sidebar_gametype, mapping_dict=dict_genre)
    mask_hours = df_vg['hours_played'].between(sidebar_hours[0], sidebar_hours[1])
    mask_perso_score = df_vg['perso_score'].between(sidebar_perso_score[0], sidebar_perso_score[1])
    mask_finish = df_vg['finished'].isin(sidebar_finish)

    # Final filtered DataFrame
    subdf_filter = df_vg[
        mask_console &
        mask_hours &
        mask_finish &
        mask_perso_score &
        mask_gametype
    ].reset_index(drop=True)

    return subdf_filter
