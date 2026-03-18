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
poetry run python scripts/seed_database.py        # seed or update gaming_lifetime (idempotent)
poetry run python scripts/import_hltb.py          # upsert how_long_to_beat from hltb_scrap.csv
poetry run python scripts/build_metacritic_merged.py  # rebuild metacritic_merged via fuzzy match
```

> **Fresh DB:** `docker-compose up --build` auto-seeds all tables via `initdb.d` (alphabetical order):
> `init.sql` (schema) → `seed.sql` (gaming_lifetime) → `seed_hltb.sql` (how_long_to_beat) → `seed_metacritic_merged.sql` (metacritic_merged).
> Re-seeding only triggers on an empty data volume — use `docker-compose down && docker-compose up --build` to force it.

### Maintenance workflow

#### Adding new games to gaming_lifetime
1. Add the new row(s) to `db_data/seed.sql` (follow the existing INSERT format)
2. Run `seed_database.py` to push changes to the live DB (idempotent — ON CONFLICT DO NOTHING skips existing rows):
```bash
docker exec py_gaming_app sh -c "DATABASE_URL=postgresql://gaming_pandas:gamer@gaming_db:5432/my_videogames python scripts/seed_database.py"
```
3. Commit `db_data/seed.sql`

#### Re-scraping HLTB (after new games added)
4. Run the HLTB scraper → replace `db_data/csv/hltb_scrap.csv` in the private data repo
5. Run `import_hltb.py` (upserts + enriches CSV with country_dev/studio/editor from gaming_lifetime):
```bash
docker exec py_gaming_app sh -c "DATABASE_URL=postgresql://gaming_pandas:gamer@gaming_db:5432/my_videogames python scripts/import_hltb.py"
```
6. Commit the updated CSV in the private data repo

#### Rebuilding metacritic_merged (after new games added)
7. Optionally add new scraped CSVs to `db_data/csv/`
8. Run `build_metacritic_merged.py` (TRUNCATE + rebuild + export `metacritic_merged_local.csv`):
```bash
docker exec py_gaming_app sh -c "DATABASE_URL=postgresql://gaming_pandas:gamer@gaming_db:5432/my_videogames python scripts/build_metacritic_merged.py"
```
9. Commit the updated `metacritic_merged_local.csv` in the private data repo

#### Syncing Docker seeding after private data CSVs change
```bash
docker-compose down && docker-compose up --build
```

### Access
- Streamlit app: http://localhost:8501
- PostgreSQL: localhost:5432

## 3. Current Architecture & WIP Goals
- **Project State**: In active development. All 3 pages functional.
**Completed**
- Refactor of all 3 pages — logic moved out of `pages/` into `functions/` modules
- Fuzzy matching (`rapidfuzz`, `build_metacritic_merged.py`)
- Dynamic SQL system for adding new games (`seed.sql` + idempotent `seed_database.py`)
**Next**
- Dynamic SQL form in Streamlit (add new games via UI)

### Two-container Docker setup
- **gaming_db**: PostgreSQL 16 Alpine — `init.sql` (schema) + `seed.sql` + `seed_hltb.sql` + `seed_metacritic_merged.sql` all auto-run via `initdb.d` on a fresh volume.
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
| `sidebar.py` | `SidebarKeys` constants, `render_sidebar()` → returns filter dict. Uses `_int_range()` / `_sorted_unique()` helpers (NaN-safe). `country_dev`/`studio`/`editor` widgets are conditional on column presence. |
| `visualisation_tools.py` | Plotly/Matplotlib wrappers |
| `metacritic_wrangling.py` | `normalize_title()`, `fuzzymatch_metacritic()` — rapidfuzz `token_sort_ratio`, threshold 85 |

### Typical page data flow
1. `db_co.load_table('table_name')` → fetch from PostgreSQL (cached per table, no connection leaks)
2. `str_cleaning()` → `clean_df_list()` — normalize columns
3. `render_sidebar()` → `apply_filters()` — mask DataFrame
4. `analytics.*()` — compute aggregations
5. `st.plotly_chart()` / `st.dataframe()` — display

### Database tables
- **gaming_lifetime** — personal data: game_name, console, game_type, finished, played_year, hours_played, perso_score, country_dev, studio, editor, etc. (~250 games)
- **metacritic** — external: critic_score, user_score, sales data (~16K games from Kaggle + scraping)
- **how_long_to_beat** — join of gaming_lifetime + HLTB scraped data: comp_main, comp_all, comp_100, comp_plus + personal columns. `country_dev`/`studio`/`editor` added to schema; regenerate by re-running `import_hltb.py`.
- **metacritic_merged** — join of gaming_lifetime + metacritic with fuzzy match scores. `country_dev`/`studio`/`editor` added to schema; regenerate by re-running `build_metacritic_merged.py`.

### Key data conventions
- Console and game_type columns are **pipe-delimited** (e.g., `"PS4|PC"`, `"JRPG|Open World"`) — use `filter_mapping()` / `clean_df_list()` to handle them
- `Filters` is a `TypeAlias = Dict[str, Any]` (defined in `filters.py`)
- Always use `.copy()` on DataFrames before mutation
- Scores are 0–100 scale
- `str_cleaning()` in `data_wrangling.py` guards `country_dev` with `if 'country_dev' in df.columns` — not all tables have this column
- Each page must have an **empty-table guard** (`if df.empty: st.warning(...); st.stop()`) right after `load_table()` — seeds load on fresh DB only, edge cases exist

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
