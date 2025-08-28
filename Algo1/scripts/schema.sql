CREATE TABLE IF NOT EXISTS bars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,
    t_start TEXT NOT NULL,
    freq_min INTEGER NOT NULL,
    open REAL, high REAL, low REAL, close REAL,
    volume REAL, vwap REAL, n_ticks INTEGER,
    quality_flag INTEGER DEFAULT 1
);
CREATE UNIQUE INDEX IF NOT EXISTS uq_bars_symbol_interval
  ON bars(symbol, t_start, freq_min);
