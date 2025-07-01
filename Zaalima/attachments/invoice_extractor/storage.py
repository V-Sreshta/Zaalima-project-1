import pandas as pd
import sqlite3
import os

def save_to_excel(data, file):
    df = pd.DataFrame([data])
    if not os.path.exists(file):
        df.to_excel(file, index=False)
    else:
        old = pd.read_excel(file)
        new = pd.concat([old, df], ignore_index=True)
        new.to_excel(file, index=False)

def save_to_db(data, db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS invoices (
                    invoice_number TEXT PRIMARY KEY,
                    date TEXT,
                    amount REAL,
                    vendor TEXT
                )''')
    try:
        c.execute("INSERT INTO invoices VALUES (?, ?, ?, ?)", 
                  (data["invoice_number"], data["date"], data["amount"], data["vendor"]))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()

def is_duplicate(invoice_number, file):
    if not os.path.exists(file):
        return False
    df = pd.read_excel(file)
    return invoice_number in df["invoice_number"].values
