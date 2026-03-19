"""
Scrape How Long to Beat data for games in gaming_lifetime.
Outputs db_data/csv/hltb_scrap.csv (16 columns) — input for import_hltb.py.

Default mode (incremental): only scrapes games not yet in how_long_to_beat.
Use --full to re-scrape all games.

Usage (via Docker):
    # Incremental — only new games (default)
    docker exec py_gaming_app sh -c \
      "DATABASE_URL=postgresql://gaming_pandas:gamer@gaming_db:5432/my_videogames \
       python scripts/scrape_hltb.py"

    # Full re-scrape
    docker exec py_gaming_app sh -c \
      "DATABASE_URL=postgresql://gaming_pandas:gamer@gaming_db:5432/my_videogames \
       python scripts/scrape_hltb.py --full"

This is a one-shot maintenance script. Run it after adding new games to gaming_lifetime,
then run import_hltb.py to upsert the results into the how_long_to_beat table.
"""
import argparse
import os
import time

import pandas as pd
from howlongtobeatpy import HowLongToBeat
from sqlalchemy import create_engine

DB_URL = os.environ["DATABASE_URL"]
CSV_PATH = "db_data/csv/hltb_scrap.csv"
REQUEST_DELAY = 0.5  # seconds between requests (~250 games ≈ 2-3 min total)

# Map personal console names to HLTB platform names
CONSOLE_MAP = {
    "PS1": "PlayStation",
    "PS2": "PlayStation 2",
    "PS3": "PlayStation 3",
    "PS4": "PlayStation 4",
    "PS5": "PlayStation 5",
    "Switch": "Nintendo Switch",
    "GameCube": "Nintendo GameCube",
    "N64": "Nintendo 64",
    "SNES": "Super Nintendo",
    "NES": "NES",
    "GameBoy": "GameBoy",
    "GBA": "Game Boy Advance",
    "Wii": "Wii",
    "Megadrive": "Sega Mega Drive/Genesis",
    "Android": "Mobile",
    "PC": "PC",
}

GL_COLS = [
    "game_name",
    "console",
    "game_type",
    "finished",
    "published_year",
    "played_year",
    "hours_played",
    "perso_score",
    "multiplayed",
]

CSV_COL_ORDER = [
    "game_name",
    "console",
    "game_type",
    "finished",
    "published_year",
    "played_year",
    "hours_played",
    "perso_score",
    "multiplayed",
    "comp_100",
    "comp_all",
    "comp_main",
    "comp_plus",
    "platform",
    "developer",
]


def get_new_games(engine) -> pd.DataFrame:
    """Return games from gaming_lifetime not yet in how_long_to_beat."""
    cols = ", ".join(f"gl.{c}" for c in GL_COLS)
    query = f"""
        SELECT {cols}
        FROM gaming_lifetime gl
        LEFT JOIN how_long_to_beat hltb ON gl.game_name = hltb.game_name
        WHERE hltb.game_name IS NULL
    """
    return pd.read_sql(query, engine)


def scrape_games(df: pd.DataFrame) -> list:
    """Scrape HLTB data for each game in df. Returns list of row dicts."""
    hltb_client = HowLongToBeat()
    rows = []
    not_found = []

    for _, row in df.iterrows():
        game_name = row["game_name"]
        console_primary = row["console"].split("|")[0]
        platform = CONSOLE_MAP.get(console_primary, console_primary)

        print(f"  Scraping: {game_name} ({platform})")
        try:
            results = hltb_client.search(game_name)
            # best_element is the highest-similarity result, None if no results
            entry = max(results, key=lambda r: r.similarity) if results else None
        except Exception as exc:
            print(f"    ⚠ Error: {exc}")
            entry = None

        if entry is None:
            not_found.append(game_name)

        rows.append(
            {
                **row.to_dict(),
                "comp_main": entry.main_story if entry else None,
                "comp_plus": entry.main_extra if entry else None,
                "comp_100": entry.completionist if entry else None,
                "comp_all": entry.all_styles if entry else None,
                "platform": platform,
                "developer": entry.profile_dev if entry else None,
            }
        )
        time.sleep(REQUEST_DELAY)

    if not_found:
        print(f"  ⚠ Not found on HLTB ({len(not_found)}): {', '.join(not_found)}")

    return rows


def main(full: bool = False) -> None:
    engine = create_engine(DB_URL)

    if full:
        print("Mode: full re-scrape (all games)")
        df_to_scrape = pd.read_sql(
            f"SELECT {', '.join(GL_COLS)} FROM gaming_lifetime", engine
        )
    else:
        print("Mode: incremental (new games only)")
        df_to_scrape = get_new_games(engine)

    if df_to_scrape.empty:
        print("✅ No new games to scrape — how_long_to_beat is already up to date")
        return

    print(f"Scraping {len(df_to_scrape)} game(s)...")
    new_rows = scrape_games(df_to_scrape)
    df_new = pd.DataFrame(new_rows)[CSV_COL_ORDER]

    # Incremental: merge with existing CSV so the output is always a full snapshot
    if not full and os.path.exists(CSV_PATH):
        df_existing = pd.read_csv(CSV_PATH)[CSV_COL_ORDER]
        df_out = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_out = df_new

    df_out.index = df_out.index + 1  # id starts at 1 (for seed_hltb.sql COPY)
    df_out.to_csv(CSV_PATH, index=True, index_label="id")

    matched = df_new["comp_main"].notna().sum()
    print(f"\n✅ {len(new_rows)} game(s) scraped, {matched} matched on HLTB")
    print(f"   CSV: {len(df_out)} total rows → {CSV_PATH}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Scrape HLTB data for games in gaming_lifetime"
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="Re-scrape all games (default: only new games not in how_long_to_beat)",
    )
    args = parser.parse_args()
    main(full=args.full)
