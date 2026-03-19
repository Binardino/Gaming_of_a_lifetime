"""
Scrape How Long to Beat data for all games in gaming_lifetime.
Outputs db_data/csv/hltb_scrap.csv (16 columns) — input for import_hltb.py.

Usage (via Docker):
    docker exec py_gaming_app sh -c \
      "DATABASE_URL=postgresql://gaming_pandas:gamer@gaming_db:5432/my_videogames \
       python scripts/scrape_hltb.py"

This is a one-shot maintenance script. Run it after adding new games to gaming_lifetime,
then run import_hltb.py to upsert the results into the how_long_to_beat table.
"""
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


def main():
    engine = create_engine(DB_URL)
    df_gl = pd.read_sql(f"SELECT {', '.join(GL_COLS)} FROM gaming_lifetime", engine)

    hltb_client = HowLongToBeat()
    rows = []
    not_found = []

    for _, row in df_gl.iterrows():
        game_name = row["game_name"]
        # Take first console for pipe-delimited values (e.g. "PS4|PC" → "PS4")
        console_primary = row["console"].split("|")[0]
        platform = CONSOLE_MAP.get(console_primary, console_primary)

        print(f"Scraping: {game_name} ({platform})")
        try:
            results = hltb_client.search(game_name)
            entry = max(results, key=lambda r: r.similarity) if results else None
        except Exception as exc:
            print(f"  ⚠ Error for '{game_name}': {exc}")
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

    df_out = pd.DataFrame(rows)[CSV_COL_ORDER]
    df_out.index = df_out.index + 1  # id starts at 1 (for seed_hltb.sql COPY)
    df_out.to_csv(CSV_PATH, index=True, index_label="id")

    matched = df_out["comp_main"].notna().sum()
    print(f"\n✅ {len(df_out)} games processed, {matched} matched on HLTB → {CSV_PATH}")
    if not_found:
        print(f"⚠ Not found on HLTB ({len(not_found)}): {', '.join(not_found)}")


if __name__ == "__main__":
    main()
