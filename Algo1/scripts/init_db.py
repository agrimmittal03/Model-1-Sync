import sqlite3, pathlib, sys

DB_PATH = pathlib.Path(__file__).resolve().parents[1] / "data_foundation.db"
SCHEMA  = pathlib.Path(__file__).resolve().parent / "schema.sql"

print("Resolved DB_PATH:", DB_PATH)
print("Resolved SCHEMA :", SCHEMA)
print("DB exists?      :", DB_PATH.exists())
print("SCHEMA exists?  :", SCHEMA.exists())

try:
    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA, "r", encoding="utf-8") as f:
        sql = f.read()
    conn.executescript(sql)
    conn.commit()
    conn.close()
    print("Initialized SQLite at", DB_PATH)
except Exception as e:
    print("ERROR:", repr(e))
    sys.exit(1)
