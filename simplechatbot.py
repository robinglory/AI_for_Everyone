# Load extracted text from the file
def load_text(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: Text file not found.")
        return ""

# Simple chatbot function
def chatbot():
    data = load_text(r"C:\Users\ASUS\Documents\Python\Programs\pdf_text.txt")
    
    if not data:
        print("No data available for chatbot.")
        return

    print("Chatbot is ready! Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ").lower()

        if user_input == "exit":
            print("Goodbye!")
            break

        # Search for keywords in extracted text
        if user_input in data.lower():
            print("Chatbot: I found something related to your query!\n")
            # Show a portion of the extracted text
            index = data.lower().find(user_input)
            snippet = data[index : index + 300]  # Show 300 characters around the keyword
            print(snippet)
        else:
            print("Chatbot: Sorry, I couldn't find anything related to that.")

# Run chatbot
chatbot()
