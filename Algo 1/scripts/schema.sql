-- Bars table: minimal MVP
CREATE TABLE IF NOT EXISTS bars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,            -- ticker/instrument code (e.g., RELIANCE)
    t_start TEXT NOT NULL,           -- ISO8601 bar start time (e.g., 2025-08-26T09:15:00+05:30)
    freq_min INTEGER NOT NULL,       -- bar interval in minutes: 1, 5, 60, 1440
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume REAL,                     -- sum of tick quantities in the bar
    vwap REAL,                       -- sum(p_i*q_i)/sum(q_i) within the bar
    n_ticks INTEGER,                 -- number of ticks in the bar
    quality_flag INTEGER DEFAULT 1   -- 1=complete bar; 0=partial/in-progress
);

-- prevent duplicates for same symbol+time+interval
CREATE UNIQUE INDEX IF NOT EXISTS uq_bars_symbol_interval
    ON bars(symbol, t_start, freq_min);
