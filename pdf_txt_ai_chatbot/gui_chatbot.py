import customtkinter as ctk
import google.generativeai as genai
from threading import Thread

# Configure Gemini API
genai.configure(api_key="AIzaSyDo01CBIaanACl5voE9NEm7CdjtFPp6P2c")

# Load extracted text from file
def load_text(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: PDF text file not found."

# Generate AI response using Gemini
def get_gemini_response(query, context):
    prompt = f"Based on the following document:\n\n{context}\n\nAnswer the question: {query}"

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text  # Extract response text
    except Exception as e:
        return f"Error: {e}"

# Function to handle chatbot response
def chatbot_response():
    user_input = user_entry.get().strip()
    if not user_input:
        return

    chat_display.insert("end", f"You: {user_input}\n", "user")
    user_entry.delete(0, "end")
    send_button.configure(state="disabled")  # Disable send button during response
    chat_display.insert("end", "Chatbot: Thinking...\n", "bot")
    chat_display.yview("end")

    def generate_response():
        response = get_gemini_response(user_input, pdf_text)
        chat_display.delete("end-2l", "end")  # Remove "Thinking..."
        chat_display.insert("end", f"Chatbot: {response}\n\n", "bot")
        chat_display.yview("end")
        send_button.configure(state="normal")  # Re-enable send button

    Thread(target=generate_response).start()

# Function to clear chat
def clear_chat():
    chat_display.delete("1.0", "end")

# Load PDF text
pdf_text = load_text(r"C:\Users\ASUS\Documents\Python\Programs\amecal_txt.txt")

# Create GUI Window
ctk.set_appearance_mode("dark")  # Dark Mode
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Advanced AI Chatbot (Gemini)")
root.geometry("600x700")

# Chat Display Area
chat_display = ctk.CTkTextbox(root, width=550, height=500, wrap="word", font=("Arial", 14))
chat_display.pack(pady=10, padx=10)
chat_display.tag_config("user", foreground="cyan")
chat_display.tag_config("bot", foreground="lightgreen")

# User Input Field
user_entry = ctk.CTkEntry(root, width=450, font=("Arial", 14))
user_entry.pack(pady=5, padx=10, side="left")

# Send Button
send_button = ctk.CTkButton(root, text="Send", command=chatbot_response, font=("Arial", 14), corner_radius=10)
send_button.pack(pady=5, side="right")

# Clear Chat Button
clear_button = ctk.CTkButton(root, text="Clear Chat", command=clear_chat, font=("Arial", 14), corner_radius=10)
clear_button.pack(pady=5)

# Bind "Enter" Key to Send Message
def enter_key(event):
    chatbot_response()

root.bind("<Return>", enter_key)

# Run GUI
root.mainloop()


