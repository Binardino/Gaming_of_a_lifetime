import pandas as pd
from sqlalchemy import create_engine
from functions.db_import_utils import upsert_dataframe
import os

DB_URL = os.environ["DATABASE_URL"]
CSV_PATH = "db_data/csv/hltb_scrap.csv"

def main():
    engine = create_engine(DB_URL)
    df = pd.read_csv(CSV_PATH)

    upsert_dataframe(
        df=df,
        table="how_long_to_beat",
        engine=engine,
        conflict_cols=["game_name", "platform"],
    )

    print(f"✅ {len(df)} rows processed")

if __name__ == "__main__":
    main()
