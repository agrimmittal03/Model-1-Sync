import sqlite3, pathlib
import pandas as pd

DB_PATH = pathlib.Path(__file__).resolve().parents[1] / "data_foundation.db"
OUT_PATH = pathlib.Path(__file__).resolve().parents[1] / "excel" / "bars.parquet"
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

with sqlite3.connect(DB_PATH) as conn:
    df = pd.read_sql_query(
        """
        SELECT symbol, t_start, freq_min, open, high, low, close,
               volume, vwap, n_ticks, quality_flag
        FROM bars
        ORDER BY t_start
        """,
        conn
    )

df.to_parquet(OUT_PATH, index=False)  # writes a single Parquet file
print(f"Wrote {len(df)} rows to {OUT_PATH}")
