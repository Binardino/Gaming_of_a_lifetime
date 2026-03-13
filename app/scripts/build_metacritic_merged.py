"""
build_metacritic_merged.py

Rebuilds the metacritic_merged table by fuzzy-matching gaming_lifetime games
against the metacritic catalog (Kaggle 2016 + scraped CSVs), blocked by console.

Usage:
    poetry run python scripts/build_metacritic_merged.py

Requires DATABASE_URL in the environment (or a .env file at the project root).
"""

import os
import sys
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from tqdm import tqdm

sys.path.append(str(Path(__file__).resolve().parent.parent))
from functions.metacritic_wrangling import fuzzymatch_metacritic

load_dotenv()

# Repo root is 2 levels above app/scripts/
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CSV_DIR   = REPO_ROOT / "db_data" / "csv"

KAGGLE_CSV = CSV_DIR / "metacritic_6900_games_22_Dec_2016_updated.csv"

# Scraped CSVs (filename → platform value used in the file)
SCRAPED_CSVS = [
    "meta_scraper_ps2.csv",
    "meta_scraper_ps4.csv",
    "meta_scraper_ps5.csv",
    "meta_scraper_gamecube.csv",
    "meta_scraper_nintendo-switch.csv",
    "meta_scraper_switch.csv",
    "meta_scraper_pc.csv",
    "meta_scraper_3ds.csv",
]

# Column rename for the Kaggle CSV to match scraped CSV / metacritic_merged schema
KAGGLE_COL_MAPPER = {
    'Name'            : 'game_title',
    'Platform'        : 'game_platform',
    'Year_of_Release' : 'game_release_date',
    'Critic_Score'    : 'metascore',
    'User_Score'      : 'user_score',
}

CONSOLE_MAPPER = {
    'PlayStation 4' : 'PS4',
    'PlayStation 5' : 'PS5',
    'PlayStation 2' : 'PS2',
    'PlayStation'   : 'PS1',
    'PS'            : 'PS1',
    'ps2'           : 'PS2',
    'ps4'           : 'PS4',
    'ps5'           : 'PS5',
    'pS5'           : 'PS5',
    'PC'            : 'PC',
    'pc'            : 'PC',
    'nintendo-switch': 'Switch',
    'Nintendo Switch': 'Switch',
    'switch'         : 'Switch',
    'GameCube'       : 'GameCube',
    'gamecube'       : 'GameCube',
    '3ds'            : '3DS',
    'GB'             : 'GameBoy',
    'GEN'            : 'Megadrive',
}

# Exact column order expected by metacritic_merged (matches init.sql schema)
MERGED_COLUMNS = [
    'id', 'game_name', 'console', 'game_type', 'finished',
    'published_year', 'played_year', 'hours_played', 'perso_score', 'multiplayed',
    'fuzz', 'game_title', 'game_platform', 'game_release_date',
    'Genre', 'Publisher',
    'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales',
    'metascore', 'Critic_Count', 'user_score', 'User_Count',
    'Developer', 'Rating', 'game_summary',
]


def load_metacritic_from_csvs() -> pd.DataFrame:
    """Load and concat Kaggle 2016 + all available scraped CSVs."""
    df_kaggle = pd.read_csv(KAGGLE_CSV)
    df_kaggle.rename(columns=KAGGLE_COL_MAPPER, inplace=True)

    frames = [df_kaggle]
    for filename in SCRAPED_CSVS:
        path = CSV_DIR / filename
        if path.exists():
            frames.append(pd.read_csv(path))
        else:
            print(f"  [skip] {filename} not found")

    return pd.concat(frames, ignore_index=True)


def main():
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        raise RuntimeError("DATABASE_URL environment variable not set")

    engine = create_engine(db_url)

    # --- Load gaming_lifetime from DB ---
    print("Loading gaming_lifetime from DB...")
    with engine.connect() as conn:
        df_vg = pd.read_sql("SELECT * FROM gaming_lifetime", conn)

    # --- Load metacritic from CSVs ---
    print("Loading metacritic from CSVs...")
    df_meta = load_metacritic_from_csvs()

    # --- Normalize ---
    df_vg = df_vg.copy()
    df_vg['console'] = df_vg['console'].str.split('|').str[0].replace(CONSOLE_MAPPER)

    df_meta['game_platform'] = df_meta['game_platform'].replace(CONSOLE_MAPPER)
    df_meta['game_title']    = df_meta['game_title'].fillna('')

    # Numeric coercion for sales / score columns (may contain "N/A" strings)
    for col in ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales',
                'metascore', 'Critic_Count', 'user_score', 'User_Count']:
        if col in df_meta.columns:
            df_meta[col] = pd.to_numeric(df_meta[col], errors='coerce')

    df_meta_clean = df_meta.drop_duplicates(['game_title', 'game_platform'])

    # --- Fuzzy match blocked by console ---
    print(f"Fuzzy matching {len(df_vg)} personal games...")
    tqdm.pandas()

    def match_within_console(row):
        candidates = df_meta_clean.loc[
            df_meta_clean['game_platform'] == row['console'], 'game_title'
        ].reset_index(drop=True)
        if candidates.empty:
            return ""
        match, _score = fuzzymatch_metacritic(row['game_name'], candidates)
        return match

    df_vg['fuzz'] = df_vg.progress_apply(match_within_console, axis=1)

    # --- Merge ---
    df_merge = pd.merge(
        df_vg[df_vg['fuzz'] != ''],
        df_meta_clean,
        left_on=['fuzz', 'console'],
        right_on=['game_title', 'game_platform'],
        how='inner',
    )

    # --- Stats ---
    matched   = len(df_merge)
    total     = len(df_vg)
    unmatched = df_vg[df_vg['fuzz'] == ''][['game_name', 'console']]
    print(f"\n✅ Matched  : {matched}/{total}")
    print(f"❌ Unmatched: {total - matched}")
    if not unmatched.empty:
        print("\nUnmatched games:")
        print(unmatched.to_string(index=False))

    # --- Select only columns that exist in metacritic_merged schema ---
    existing_cols = [c for c in MERGED_COLUMNS if c in df_merge.columns]
    df_out = df_merge[existing_cols]

    # --- Rebuild table (truncate + insert) ---
    print("\nRebuilding metacritic_merged table...")
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE metacritic_merged"))

    df_out.to_sql('metacritic_merged', engine, if_exists='append', index=False, method='multi')
    print(f"✅ metacritic_merged rebuilt with {len(df_out)} rows")


if __name__ == "__main__":
    main()
