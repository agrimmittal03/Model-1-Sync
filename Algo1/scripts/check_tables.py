# scripts/check_tables.py
import sqlite3, pathlib, os
DB_PATH = pathlib.Path(__file__).resolve().parents[1] / "data_foundation.db"
print("Using DB:", DB_PATH)
print("Exists?:", DB_PATH.exists(), "Size (bytes):", DB_PATH.stat().st_size if DB_PATH.exists() else 0)

conn = sqlite3.connect(DB_PATH)
rows = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print("Tables:", rows)
conn.close()
