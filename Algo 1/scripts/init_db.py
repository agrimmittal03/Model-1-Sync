import sqlite3, pathlib

DB_PATH = pathlib.Path(__file__).resolve().parents[1] / "data_foundation.db"
SCHEMA  = pathlib.Path(__file__).resolve().parent / "schema.sql"

def main():
    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print(f"Initialized SQLite at {DB_PATH}")

if __name__ == "__main__":
    main()
