import google.generativeai as genai

# Set up Gemini API key
genai.configure(api_key="AIzaSyDo01CBIaanACl5voE9NEm7CdjtFPp6P2c")

# Load extracted text from file
def load_text(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: Text file not found.")
        return ""

# Generate AI response using Gemini
def get_gemini_response(query, context):
    prompt = f"Based on the following document:\n\n{context}\n\nAnswer the question: {query}"

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text  # Extract response text
    except Exception as e:
        return f"Error: {e}"

# Chatbot function
def chatbot():
    pdf_text = load_text(r"C:\Users\ASUS\Documents\Python\Programs\pdf_txt_ai_chatbot\scholarship.txt")

    if not pdf_text:
        print("No data available for chatbot.")
        return

    print("Gemini AI Chatbot is ready! Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = get_gemini_response(user_input, pdf_text)
        print(f"Chatbot: {response}")

# Run chatbot
chatbot()

