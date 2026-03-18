from sqlalchemy import create_engine, text
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

DB_URL = os.environ.get("DATABASE_URL")

SEED_SQL_PATH = Path(__file__).resolve().parents[2] / "db_data" / "seed.sql"


def main():
    """
    Seed or update gaming_lifetime from seed.sql.
    Idempotent: ON CONFLICT DO NOTHING in seed.sql prevents duplicates.
    Safe to re-run after adding new games to seed.sql.
    """
    if not DB_URL:
        raise RuntimeError("DATABASE_URL environment variable not set")

    if not SEED_SQL_PATH.exists():
        raise FileNotFoundError(f"seed.sql not found at {SEED_SQL_PATH}")

    engine = create_engine(DB_URL)

    with open(SEED_SQL_PATH, "r", encoding="utf-8") as f:
        seed_sql = f.read()

    with engine.begin() as conn:
        conn.execute(text(seed_sql))

    print("✅ Database seeded successfully")


if __name__ == "__main__":
    main()
