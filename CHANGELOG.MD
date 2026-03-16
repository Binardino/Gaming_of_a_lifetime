All notable changes to this project will be documented in this file.

## [0.5.0] – 2026-03-13
Refactor page 2_metacritic + generic `load_table()` + fuzzy matching improvement

### Added
- `metacritic_wrangling.py` : `normalize_title()` + `fuzzymatch_metacritic()` via `rapidfuzz` (token_sort_ratio, threshold 85) — remplace `difflib.SequenceMatcher` (95%)
- `scripts/build_metacritic_merged.py` : nouveau script pour rebuilder `metacritic_merged` — fuzzy match bloqué par console, lecture Kaggle CSV + scraped CSVs, TRUNCATE + INSERT
- `rapidfuzz >= 3.0` ajouté aux dépendances (`pyproject.toml`)

### Changed
- `db_connection.py` : `load_gaming_lifetime()` remplacée par `load_table(table_name)` générique — un seul point d'entrée pour toutes les tables, `@st.cache_data` cache par argument
- `pages/1_app_gaming.py` : appel mis à jour vers `load_table('gaming_lifetime')`
- `pages/2_metacritic.py` : refactor complet — imports explicites, 3 connexions DB non fermées corrigées, sidebar NameError corrigé (`render_sidebar()` + `apply_filters()`), markdown et labels fixes

### Removed
- `functions/mask_df_utils.py` supprimé — système de filtres obsolète incompatible avec `sidebar.py` / `filters.py`

## [0.4.0] – 2026-03-12
Refactor page 1_app_gaming + module DB connection

### Added
- `db_connection.py` : `load_gaming_lifetime()` avec `@st.cache_data` et context manager — remplace l'ancien système de connexion inline
- `BRAND_COLOUR_MAP` constant dans `1_app_gaming.py`

### Changed
- `pages/1_app_gaming.py` : connexion DB legacy supprimée, remplacée par `db_co.load_gaming_lifetime()`
- Imports wildcard remplacés par imports explicites
- Fix typo sur les clés de filtres (`f_hours_played`, `f_perso_score` — ne correspondaient pas à `filters.py`)

## [0.3.0] – 2025-12-24
Refactor of page 1_app_gaming.py
### Added
- Refactored Streamlit architecture (add modules sidebar / filters)
- New analytics module with pandas-only logic
- Add new analysis

### Changed
- Improved filtering system and data cleaning
- Clear separation between computation and visualisation