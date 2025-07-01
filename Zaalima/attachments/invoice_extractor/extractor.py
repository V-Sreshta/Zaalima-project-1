import pdfplumber
import re

def extract_invoice_data(filepath):
    with pdfplumber.open(filepath) as pdf:
        text = ''.join([page.extract_text() for page in pdf.pages if page.extract_text()])

    invoice_number = re.search(r"Invoice\s*#?:?\s*(\w+)", text)
    date = re.search(r"Date:?\s*([\d/-]+)", text)
    amount = re.search(r"Total\s*Amount:?\s*[$₹]?([\d,]+\.\d{2})", text)
    vendor = re.search(r"Vendor:?\s*(.+)", text)

    if not all([invoice_number, date, amount, vendor]):
        return None

    return {
        "invoice_number": invoice_number.group(1),
        "date": date.group(1),
        "amount": amount.group(1).replace(",", ""),
        "vendor": vendor.group(1).strip()
    }
