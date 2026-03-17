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

#%% Load data
df_hltb_raw = db_co.load_table('how_long_to_beat')

if df_hltb_raw.empty:
    st.warning(
        "No How Long To Beat data available yet. "
        "The dataset has not been loaded into the database."
    )
    st.info(
        "**For admins:** populate the table by running the import script inside the app container:\n\n"
        "```bash\n"
        "docker exec py_gaming_app sh -c "
        "\"DATABASE_URL=postgresql://<user>:<password>@gaming_db:<port>/<db> "
        "python scripts/import_hltb.py\"\n"
        "```"
    )
    st.stop()

#%% Clean + extract lists
df_hltb = str_cleaning(df_hltb_raw)
_, console_list, dict_console = clean_df_list(df_hltb, 'console')
_, genre_list,   dict_genre   = clean_df_list(df_hltb, 'game_type')

#%% Sidebar + filters
filters      = render_sidebar(df_vg=df_hltb, console_list=console_list, genre_list=genre_list)
subdf_filter = apply_filters(df=df_hltb, filters=filters,
                             dict_console=dict_console, dict_genre=dict_genre)

#%% Computed columns (on filtered df)
subdf_filter = subdf_filter.copy()
subdf_filter['main_diff'] = subdf_filter['comp_main'] - subdf_filter['hours_played']
subdf_filter['plus_diff'] = subdf_filter['comp_plus'] - subdf_filter['hours_played']

#%% README
st.write("# How Long To Beat — Comparison 🎮")
st.markdown(f"""# Welcome to the Adventure of a Lifetime - How long to beat comparison🎮
            
The goal of this part is to compare my personal data from my videogame_lifetime database with the data from How Long To Beat (HLTB). 
HLTB is an crowd sourced database, agregating the time the players took to finish a game. 

**Compare data from HLTB dataset**

The available How Long To Beat is up-to-date with data fetching ;

List how long takes a game to be done at various stages. Only the {df_hltb.size}

Compare personal gaming data against the [How Long To Beat](https://howlongtobeat.com/) dataset.
HLTB is a crowd-sourced database aggregating the time players took to complete a game.

**Completion time categories:**
- `comp_main` — main story only
- `comp_plus` — main story + extras
- `comp_all` — all achievements / side content
- `comp_100` — 100% completion

Dataset: **{len(subdf_filter)} games** matched after filters.
""")

#%% Chart 1 — Scatter: personal hours vs HLTB main completion time
st.subheader("Personal hours played vs HLTB main completion time — by game type")
st.write("Scatter plot comparing time I actually spent vs the average main story completion time from HLTB.")

fig_scatter = px.scatter(
    data_frame=subdf_filter,
    x='hours_played',
    y='comp_main',
    color='game_type',
    hover_name='game_name',
)
st.plotly_chart(fig_scatter)

#%% Chart 2 — Violin: hours_played vs comp_all distribution by game name
st.subheader("Personal hours vs full completion time — distribution by game")
st.write("Violin plot showing the spread between personal hours played and HLTB all-achievements time, per game.")

fig_violin_by_game = px.violin(
    data_frame=subdf_filter,
    x='game_name',
    y=['hours_played', 'comp_all'],
    box=True,
)
st.plotly_chart(fig_violin_by_game)

#%% Chart 3 — Box: hours_played vs comp_all by game name, colored by platform
st.subheader("Personal hours vs full completion time — box plot by game and platform")
st.write("Box plot of personal hours vs HLTB all-achievements time, broken down by game and HLTB platform.")

fig_boxplot = px.box(
    data_frame=subdf_filter,
    x='game_name',
    y=['hours_played', 'comp_all'],
    width=1000, height=400,
    color='platform',
)
st.plotly_chart(fig_boxplot)

#%% Chart 4 — Violin: main+extras time difference by game type
st.subheader("Main + extras hours difference (personal vs HLTB) — by game type")
st.write("Violin plot of the difference between my playtime and HLTB main+extras time, per genre.")

fig_violin_diff = px.violin(
    subdf_filter,
    x='game_type',
    y='plus_diff',
    color='game_type',
    title='Violin: Main+Plus hours difference per game type',
    box=True,
)
st.plotly_chart(fig_violin_diff)

#%% Chart 5 — Strip: main+extras time difference by game type
st.subheader("Main + extras hours difference — strip plot by game type")
st.write("Individual data points showing the difference between my playtime and HLTB main+extras time.")

fig_strip = px.strip(
    subdf_filter,
    x='game_type',
    y='plus_diff',
    hover_name='game_name',
    color='game_type',
    title='Strip plot: Main+Plus hours difference by game type',
    width=800,
)
st.plotly_chart(fig_strip)

#%% Chart 6 — Polar: main completion time by game
st.subheader("HLTB main completion time — polar chart by game")
st.write("Polar chart showing main story completion time from HLTB for each matched game.")

fig_radar = px.line_polar(
    subdf_filter,
    r='comp_main',
    theta='game_name',
    line_close=True,
)
st.plotly_chart(fig_radar)
