import sqlite3

def init_db():
    conn = sqlite3.connect('data/billwise.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS receipts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vendor TEXT,
            date TEXT,
            amount REAL,
            category TEXT,
            raw_text TEXT,
            file_path TEXT
        );
    ''')
    # Add index for search efficiency
    c.execute('CREATE INDEX IF NOT EXISTS idx_vendor ON receipts (vendor);')
    c.execute('CREATE INDEX IF NOT EXISTS idx_date ON receipts (date);')
    c.execute('CREATE INDEX IF NOT EXISTS idx_amount ON receipts (amount);')
    conn.commit()
    conn.close()