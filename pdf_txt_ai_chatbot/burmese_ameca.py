import customtkinter as ctk
import google.generativeai as genai
import speech_recognition as sr
import pygame
from gtts import gTTS
from threading import Thread
import os
from googletrans import Translator

# Configure Gemini API
genai.configure(api_key="AIzaSyBRG35ZZwUDaO7Hi8VI4GTCD6AjuUW6xoI")

# Initialize Translator for Burmese
translator = Translator()

# Load extracted text from file
def load_text(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: PDF text file not found."

# Generate AI response using Gemini
def get_gemini_response(query, context):
    prompt = f"Based on the following document:\n\n{context}\n\nAnswer in Burmese: {query}"
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text  # Extract response text
    except Exception as e:
        return f"Error: {e}"

# Convert text to speech (Burmese)
def speak(text):
    if not text.strip():
        return  # Don't try to speak empty responses

    try:
        tts = gTTS(text=text, lang="my")
        audio_file = "response.mp3"
        tts.save(audio_file)

        # Reinitialize pygame each time to prevent audio issues
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # Stop the mixer and unload the file
        pygame.mixer.music.stop()
        pygame.mixer.quit()

        # Wait a short moment to ensure file is released
        pygame.time.delay(100)

        # Delete the file safely
        if os.path.exists(audio_file):
            os.remove(audio_file)
    except Exception as e:
        print("Error in voice output:", e)

# Listen for voice input (Burmese)
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        chat_display.insert("end", "🎤 Listening...\n", "bot")
        chat_display.yview("end")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio, language="my")  # Use Burmese language
            return text
        except sr.UnknownValueError:
            return "မဖတ်နိုင်ပါ"
        except sr.RequestError:
            return "Could not request results, please check your connection."

# Handle chatbot response
def chatbot_response(user_input):
    if not user_input:
        return

    # Detect input language and translate to English
    detected_lang = translator.detect(user_input).lang
    if detected_lang != "en":
        user_input_en = translator.translate(user_input, src=detected_lang, dest="en").text
    else:
        user_input_en = user_input
    
    chat_display.insert("end", f"🧑‍💻 You: {user_input}\n\n", "user")
    chat_display.insert("end", "🤖 Chatbot: Thinking...\n", "bot")
    chat_display.yview("end")

    def generate_response():
        response_en = get_gemini_response(user_input_en, pdf_text)
        # Translate response back to Burmese
        response_my = translator.translate(response_en, src="en", dest="my").text

        chat_display.delete("end-2l", "end")  # Remove "Thinking..."
        chat_display.insert("end", f"🤖 Chatbot: {response_my}\n\n", "bot")
        chat_display.yview("end")
        speak(response_my)  # Speak the response in Burmese

    Thread(target=generate_response).start()

# Function to handle voice input
def voice_input():
    user_input = listen()
    user_entry.delete(0, "end")
    user_entry.insert(0, user_input)  # Show recognized text in input field
    chatbot_response(user_input)

# Function to send text input
def text_input():
    user_input = user_entry.get().strip()
    user_entry.delete(0, "end")
    chatbot_response(user_input)

# Function to clear chat
def clear_chat():
    chat_display.delete("1.0", "end")

# Load PDF text
pdf_text = load_text(r"C:\Users\ASUS\Documents\Python\Programs\pdf_txt_ai_chatbot\amecal_txt.txt")

# Create GUI Window
ctk.set_appearance_mode("dark")  # Dark Mode
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("AI Chatbot with Voice (Gemini)")
root.geometry("600x700")

# Chat Display Area
chat_display = ctk.CTkTextbox(root, width=550, height=500, wrap="word", font=("Arial", 14))
chat_display.pack(pady=10)
chat_display.tag_config("user", foreground="cyan")
chat_display.tag_config("bot", foreground="lightgreen")

# User Input Field
user_entry = ctk.CTkEntry(root, width=400, font=("Arial", 14))
user_entry.pack(pady=5)

# Button Frame
button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=5)

# Send Button
send_button = ctk.CTkButton(button_frame, text="Send", command=text_input, font=("Arial", 14), corner_radius=10)
send_button.grid(row=0, column=0, padx=5)

# Voice Button
voice_button = ctk.CTkButton(button_frame, text="🎤 Speak", command=voice_input, font=("Arial", 14), corner_radius=10)
voice_button.grid(row=0, column=1, padx=5)

# Clear Chat Button
clear_button = ctk.CTkButton(root, text="Clear Chat", command=clear_chat, font=("Arial", 14), corner_radius=10)
clear_button.pack(pady=5)

# Bind "Enter" Key to Send Message
def enter_key(event):
    text_input()

root.bind("<Return>", enter_key)

# Run GUI
root.mainloop()
