import pandas as pd
import PyPDF2 
with open("C:/Users/neela/OneDrive/Desktop/Pythonnotes.pdf",'rb') as f:
    text=PyPDF2.PdfReader(f)
    for i in range(len(text.pages)):
        pages=text.pages[i]
        content_pages=pages.extract_text()
        print(content_pages)
        