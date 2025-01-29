from pypdf import PdfReader

# Define file path
pdf_path = r"C:\Users\ASUS\Documents\Python\Programs\amecal.pdf"
output_txt_path = r"C:\Users\ASUS\Documents\Python\Programs\amecal_txt.txt"

try:
    reader = PdfReader(pdf_path)
    
    # Extract text from all pages
    extracted_text = ""
    for page in reader.pages:
        extracted_text += page.extract_text() + "\n\n"

    # Save extracted text to a file
    with open(output_txt_path, "w", encoding="utf-8") as file:
        file.write(extracted_text)

    print("Text extracted and saved successfully!")

except FileNotFoundError:
    print("Error: The PDF file was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
