import os
from extractor import extract_invoice_data
from storage import save_to_excel, save_to_db, is_duplicate
from reports import generate_monthly_report, generate_vendor_summary

PDF_DIR = "invoices"
EXCEL_FILE = "data/invoices.xlsx"
DB_FILE = "data/invoices.db"

def main():
    for filename in os.listdir(PDF_DIR):
        if filename.endswith(".pdf"):
            filepath = os.path.join(PDF_DIR, filename)
            data = extract_invoice_data(filepath)
            if data and not is_duplicate(data["invoice_number"], EXCEL_FILE):
                save_to_excel(data, EXCEL_FILE)
                save_to_db(data, DB_FILE)

    # Generate reports
    generate_monthly_report(DB_FILE)
    generate_vendor_summary(DB_FILE)

if __name__ == "__main__":
    main()
