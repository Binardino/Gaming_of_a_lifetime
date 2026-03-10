# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Gaming of a Lifetime** is a Streamlit analytics web app for visualizing personal video game history. It combines personal gaming data with external datasets (Metacritic, How Long to Beat) stored in PostgreSQL.

## Commands

### Run the full stack (recommended)
```bash
docker-compose up --build
```

### Run locally (without Docker)
```bash
cd app/
poetry install
poetry run streamlit run home_page.py --server.port=8501
```

### Code quality
```bash
cd app/
poetry run ruff check .
poetry run black --check .
poetry run mypy functions/
```

### Database scripts
```bash
cd app/
poetry run python scripts/seed_database.py
poetry run python scripts/import_metacritic.py
poetry run python scripts/import_hltb.py
```

### Access
- Streamlit app: http://localhost:8501
- PostgreSQL: localhost:5432

## Architecture

### Two-container Docker setup
- **gaming_db**: PostgreSQL 16 Alpine — initialized from `db_data/init.sql` (schema) and `db_data/seed.sql` (250+ games). CSV files are copied into the container for import scripts.
- **py_gaming_app**: Python 3.11 Streamlit app — depends on DB healthcheck before starting.

### Multi-page Streamlit app (`app/`)
- `home_page.py` — entry point / landing page
- `pages/1_app_gaming.py` — main EDA dashboard (personal gaming data)
- `pages/2_metacritic.py` — compare personal scores vs. Metacritic critic/user scores
- `pages/3_how_long_to_beat.py` — game completion time analysis

### Business logic modules (`app/functions/`)
| Module | Responsibility |
|---|---|
| `db_connection.py` | SQLAlchemy engine from `.env`, `get_data_sql()` / `get_data_csv()` |
| `data_wrangling.py` | String cleaning, pipe-delimited column splitting, console brand tagging |
| `filters.py` | Filter dispatcher (`apply_filters()`), handles pipe-delimited multi-values |
| `analytics.py` | GroupBy/pivot computations (games per console, hours, abandon rate, etc.) |
| `sidebar.py` | `SidebarKeys` constants, `render_sidebar()` → returns filter dict |
| `visualisation_tools.py` | Plotly/Matplotlib wrappers |
| `mask_df_utils.py` | Boolean masking helpers |

### Typical page data flow
1. `sql_connection()` → fetch from PostgreSQL
2. `str_cleaning()` → `clean_df_list()` — normalize columns
3. `render_sidebar()` → `apply_filters()` — mask DataFrame
4. `analytics.*()` — compute aggregations
5. `st.plotly_chart()` / `st.dataframe()` — display

### Database tables
- **gaming_lifetime** — personal data: game_name, console, game_type, finished, played_year, hours_played, perso_score, studio, etc. (~250 games)
- **metacritic** — external: critic_score, user_score, sales data (~16K games from Kaggle + scraping)
- **how_long_to_beat** — completion times: comp_main, comp_all, comp_100, comp_plus
- **metacritic_merged** — join of gaming_lifetime + metacritic with fuzzy match scores

### Key data conventions
- Console and game_type columns are **pipe-delimited** (e.g., `"PS4|PC"`, `"JRPG|Open World"`) — use `filter_mapping()` / `clean_df_list()` to handle them
- `Filters` is a `TypeAlias = Dict[str, Any]` (defined in `filters.py`)
- Always use `.copy()` on DataFrames before mutation
- Scores are 0–100 scale

## Environment

Copy `.env.example` to `.env` and fill in the values:
```
POSTGRES_DRIVER=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
POSTGRES_PORT=
POSTGRES_HOST=
POSTGRES_TABLE=
STAPP_PORT=
MOUNT_PATH=
```

`MOUNT_PATH` must point to the repo root for Docker volume mounts to work on your machine.
