# Importing required module
from pypdf import PdfReader

# Define file path
pdf_path = r"C:\Users\ASUS\Documents\Python\Programs\amecal.pdf"

try:
    # Creating a pdf reader object
    reader = PdfReader(pdf_path)

    # Printing number of pages in the PDF file
    print(f"Total Pages: {len(reader.pages)}")

    # Extracting text from the first two pages (if they exist)
    text = reader.pages[0].extract_text() if len(reader.pages) > 0 else "No text found"
    text1 = reader.pages[1].extract_text() if len(reader.pages) > 1 else "No second page"

    # Printing extracted text
    print(f"This is the sample text:\n{text}\n{text1}")

except FileNotFoundError:
    print("Error: The PDF file was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
