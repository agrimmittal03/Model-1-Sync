import sqlite3

conn = sqlite3.connect("data_foundation.db")

conn.execute(
    "INSERT INTO bars(symbol,t_start,freq_min,open,high,low,close,volume,vwap,n_ticks,quality_flag) "
    "VALUES (?,?,?,?,?,?,?,?,?,?,?)",
    ("RELIANCE","2025-08-26T09:15:00+05:30",1,2500.0,2505.0,2495.0,2502.5,10000,2501.2,42,1)
)

conn.commit()

rows = conn.execute("SELECT symbol, t_start, freq_min, open, close FROM bars").fetchall()
conn.close()

print("Rows now:", rows)
