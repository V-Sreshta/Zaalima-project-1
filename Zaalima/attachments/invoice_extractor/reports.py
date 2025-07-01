import sqlite3
import pandas as pd

def generate_monthly_report(db_file):
    conn = sqlite3.connect(db_file)
    df = pd.read_sql("SELECT * FROM invoices", conn)
    df['month'] = pd.to_datetime(df['date'], errors='coerce').dt.to_period('M')
    report = df.groupby('month')['amount'].sum().reset_index()
    report.to_csv("data/monthly_report.csv", index=False)
    conn.close()

def generate_vendor_summary(db_file):
    conn = sqlite3.connect(db_file)
    df = pd.read_sql("SELECT * FROM invoices", conn)
    report = df.groupby('vendor')['amount'].sum().reset_index()
    report.to_csv("data/vendor_summary.csv", index=False)
    conn.close()
