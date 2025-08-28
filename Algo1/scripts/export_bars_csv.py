import sqlite3, csv, pathlib

# Variables
DB_PATH = pathlib.Path(__file__).resolve().parents[1] / "data_foundation.db"
CSV_PATH = pathlib.Path(__file__).resolve().parents[1] / "excel" / "bars_view.csv"

CSV_PATH.parent.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("""
    SELECT symbol, t_start, freq_min, open, high, low, close, volume, vwap, n_ticks, quality_flag
    FROM bars
    ORDER BY t_start
""")
rows = cur.fetchall()
cols = [d[0] for d in cur.description]
conn.close()

with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(cols)
    w.writerows(rows)

print(f"Wrote {len(rows)} rows to {CSV_PATH}")
