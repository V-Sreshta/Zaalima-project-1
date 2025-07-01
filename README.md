# 📥 Invoice PDF Extractor

A smart desktop assistant built with Python that automatically logs into Gmail, fetches invoice PDFs, extracts structured data, and lets you export everything to CSV — all through a simple GUI!

---

## ✨ Features

- 📧 Connects to Gmail securely via IMAP  
- 📎 Downloads only PDF attachments from emails with subject "Invoice"  
- 🔍 Parses key-value pairs from invoices (like Invoice No, Date, Amount)  
- 🖥 Displays extracted data in a user-friendly table GUI  
- 💾 Export to CSV with one click  
- 🔒 Secure login using app-password (no hardcoding credentials)  
- 📜 Automatic log file for debugging/troubleshooting  

---

## 📂 Project Structure

Zaalima/
├── attachments/ # Folder containing downloaded PDF attachments
│ └── dummyinvoice.pdf # Example/dummy invoice for testing
├── build/
│ └── ui/ # Compiled UI assets (e.g., from PyInstaller or PyQt)
├── invoice_extractor/ # Core extraction logic (PDF/Email/Regex handling)
├── email_read.py # Handles IMAP login and reading Gmail for attachments
├── regex.py # Regex-based key-value data extractor from PDFs
├── sql_connection.py # Optional: connects and saves extracted data to a database
├── librarymanagement.py # Possibly a shared module or legacy code (rename if unused)
├── test.py # Test script to validate parsing or email logic
├── ui.py # GUI interface code (e.g., built with Tkinter/PyQt)
├── ui.spec # PyInstaller or PyQt5 spec file for packaging the app
├── extracted_data.csv # Final CSV output after parsing invoices
├── invoice_app.log # Generated log file for debugging and error tracking
├── README.md # Project documentation (you're reading it now!)

---

## 🛠 Requirements

Install all dependencies using:

pip install -r requirements.txt
Recommended packages:
imaplib

email

PyPDF2 or pdfplumber

tkinter

pandas

getpass

logging

🚀 How to Use
🔐 Set up Gmail App Password
Enable IMAP in your Gmail settings

Generate an App Password from your Google account

▶ Run the application
python ui.py

🔑 Log in securely
Enter your Gmail and App Password when prompted
Credentials are never saved

📎 PDFs get downloaded
Only from emails with subject "Invoice"

📊 Data gets extracted
Parses Invoice No, Date, Amount, Vendor, etc.

🖼 GUI Table appears
Browse, scroll, filter, and verify parsed data

💾 Export to CSV
Click "Export" to save data to extracted_data.csv

🧠 How It Works (Behind the Scenes)
email_read.py: Connects to Gmail and downloads PDF attachments

regex.py: Extracts structured invoice data using pattern matching

ui.py: Displays parsed data in a GUI table with export option

invoice_app.log: Captures logs for troubleshooting

🔐 Security Note
Your Gmail credentials are never stored. The app uses Python’s getpass module to take input securely, and supports only App Passwords for improved security.

🧑‍💻 Made with ❤ by Sreshta
Building tools that save your time, so you can focus on what matters most.
🔗 github.com/V-Sreshta
