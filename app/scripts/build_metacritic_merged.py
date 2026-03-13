"""
build_metacritic_merged.py

Rebuilds the metacritic_merged table by fuzzy-matching gaming_lifetime games
against the metacritic catalog (blocked by console platform).

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

# Make functions/ importable when running from app/
sys.path.append(str(Path(__file__).resolve().parent.parent))
from functions.metacritic_wrangling import fuzzymatch_metacritic, normalize_title

load_dotenv()

CONSOLE_MAPPER = {
    'PlayStation 4': 'PS4',
    'PlayStation 5': 'PS5',
    'PlayStation 2': 'PS2',
    'PlayStation':   'PS1',
    'PS':            'PS1',
    'PC':            'PC',
    'pc':            'PC',
    'Nintendo Switch': 'Switch',
    'switch':          'Switch',
    'GameCube':        'GameCube',
    'gamecube':        'GameCube',
    'GB':              'GameBoy',
    'GEN':             'Megadrive',
}


def main():
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        raise RuntimeError("DATABASE_URL environment variable not set")

    engine = create_engine(db_url)

    # --- Load source tables ---
    print("Loading tables from DB...")
    with engine.connect() as conn:
        df_vg = pd.read_sql("SELECT * FROM gaming_lifetime", conn)
        df_meta = pd.read_sql("SELECT * FROM metacritic", conn)

    # --- Normalize consoles ---
    # gaming_lifetime consoles can be pipe-delimited; take only the first
    df_vg = df_vg.copy()
    df_vg['console'] = df_vg['console'].str.split('|').str[0]
    df_vg['console'] = df_vg['console'].replace(CONSOLE_MAPPER)

    df_meta = df_meta.copy()
    df_meta['platform'] = df_meta['platform'].replace(CONSOLE_MAPPER)

    # Drop duplicate (game_title, platform) pairs before matching
    df_meta_clean = df_meta.drop_duplicates(['game_name', 'platform'])

    # --- Fuzzy match blocked by console ---
    print(f"Fuzzy matching {len(df_vg)} personal games against {len(df_meta_clean)} metacritic entries...")
    tqdm.pandas()

    def match_within_console(row):
        candidates = df_meta_clean.loc[
            df_meta_clean['platform'] == row['console'], 'game_name'
        ].reset_index(drop=True)
        if candidates.empty:
            return ("", 0)
        return fuzzymatch_metacritic(row['game_name'], candidates)

    results = df_vg.progress_apply(match_within_console, axis=1)
    df_vg['fuzz']       = results.map(lambda r: r[0])
    df_vg['fuzz_score'] = results.map(lambda r: r[1])

    # --- Merge ---
    df_merge = pd.merge(
        df_vg[df_vg['fuzz'] != ''],
        df_meta_clean,
        left_on=['fuzz', 'console'],
        right_on=['game_name', 'platform'],
        how='inner',
        suffixes=('', '_meta'),
    )

    # --- Stats ---
    matched = len(df_merge)
    total   = len(df_vg)
    unmatched = df_vg[df_vg['fuzz'] == ''][['game_name', 'console']]
    print(f"\n✅ Matched  : {matched}/{total}")
    print(f"❌ Unmatched: {total - matched}")
    if not unmatched.empty:
        print("\nUnmatched games:")
        print(unmatched.to_string(index=False))

    # --- Rebuild metacritic_merged (truncate + insert) ---
    print("\nRebuilding metacritic_merged table...")
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE metacritic_merged"))

    df_merge.to_sql(
        'metacritic_merged',
        engine,
        if_exists='append',
        index=False,
        method='multi',
    )
    print(f"✅ metacritic_merged rebuilt with {len(df_merge)} rows")


if __name__ == "__main__":
    main()
