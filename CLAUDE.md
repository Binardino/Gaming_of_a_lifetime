# CLAUDE.md — Project Guide & Memory


This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 1. Guiding Principles (The Karpathy Prompt)
### 1.1 Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

### 1.2 Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

### 1.3 Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

### 1.4 Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]

## 2. Project Overview

**Gaming of a Lifetime** is a Streamlit analytics web app for visualizing personal video game history. It combines personal gaming data with external datasets (Metacritic, How Long to Beat) stored in PostgreSQL.

## Development Commands

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
poetry run python scripts/build_metacritic_merged.py
```

> **Note** : `seed.sql` is NOT auto-loaded by docker-compose (only `init.sql` is). On a fresh DB, run manually:
> ```bash
> docker cp db_data/seed.sql gaming_db:/tmp/seed.sql
> docker exec gaming_db sh -c "psql -U gaming_pandas -d my_videogames -f /tmp/seed.sql"
> ```

> **Note** : `build_metacritic_merged.py` reads CSVs from `db_data/csv/` and requires `DATABASE_URL`. When running against the Docker DB (recommended), use `docker exec`:
> ```bash
> docker exec py_gaming_app sh -c "DATABASE_URL=postgresql://gaming_pandas:gamer@gaming_db:5432/my_videogames python scripts/build_metacritic_merged.py"
> ```

### Access
- Streamlit app: http://localhost:8501
- PostgreSQL: localhost:5432

## 3. Current Architecture & WIP Goals
- **Project State**: In active development. Focus is on improving modularity and EDA features.
**Refactoring Directions**
- Move logic out of `pages/` and into `functions/` modules.
- refactor of page_3_hltb (page_2_metacritic done)
- dynamic sql system to add new game entries in the future
- fuzzy matching improvement done (`rapidfuzz`, `build_metacritic_merged.py`)

### Two-container Docker setup
- **gaming_db**: PostgreSQL 16 Alpine — initialized from `db_data/init.sql` (schema only). `seed.sql` must be loaded manually on fresh DB (see Database scripts above).
- **py_gaming_app**: Python 3.11 Streamlit app — depends on DB healthcheck before starting. Uses `ENV POETRY_VIRTUALENVS_CREATE=false` to install packages globally (not in a venv).

### Multi-page Streamlit app (`app/`)
- `home_page.py` — entry point / landing page
- `pages/1_app_gaming.py` — main EDA dashboard (personal gaming data)
- `pages/2_metacritic.py` — compare personal scores vs. Metacritic critic/user scores
- `pages/3_how_long_to_beat.py` — game completion time analysis

### Business logic modules (`app/functions/`)
| Module | Responsibility |
|---|---|
| `db_connection.py` | SQLAlchemy engine from `.env`, `load_table(table_name)` (cached), `get_data_sql()` / `get_data_csv()` |
| `data_wrangling.py` | String cleaning, pipe-delimited column splitting, console brand tagging |
| `filters.py` | Filter dispatcher (`apply_filters()`), handles pipe-delimited multi-values |
| `analytics.py` | GroupBy/pivot computations (games per console, hours, abandon rate, etc.) |
| `sidebar.py` | `SidebarKeys` constants, `render_sidebar()` → returns filter dict |
| `visualisation_tools.py` | Plotly/Matplotlib wrappers |
| `metacritic_wrangling.py` | `normalize_title()`, `fuzzymatch_metacritic()` — rapidfuzz `token_sort_ratio`, threshold 85 |

### Typical page data flow
1. `db_co.load_table('table_name')` → fetch from PostgreSQL (cached per table, no connection leaks)
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
