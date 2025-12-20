from sqlalchemy import create_engine, text
from pathlib import Path
import os

DB_URL = os.environ.get("DATABASE_URL")

SEED_SQL_PATH = Path(__file__).resolve().parents[1] / "db_data" / "seed.sql"


def check_already_seeded(engine) -> bool:
    """
    Returns True if the gaming_lifetime table already contains data.
    Used to prevent accidental reseeding.
    """
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT COUNT(*) FROM gaming_lifetime")
        ).scalar()
        return result > 0


def main():
    if not DB_URL:
        raise RuntimeError("DATABASE_URL environment variable not set")

    if not SEED_SQL_PATH.exists():
        raise FileNotFoundError(f"seed.sql not found at {SEED_SQL_PATH}")

    engine = create_engine(DB_URL)

    #SAFETY CHECK — NEVER SEED TWICE
    if check_already_seeded(engine):
        raise RuntimeError(
            "Database already seeded. Aborting to avoid duplicates."
        )

    # Read seed SQL
    with open(SEED_SQL_PATH, "r", encoding="utf-8") as f:
        seed_sql = f.read()

    # Execute seed
    with engine.begin() as conn:
        conn.execute(text(seed_sql))

    print("✅ Database seeded successfully")


if __name__ == "__main__":
    main()
