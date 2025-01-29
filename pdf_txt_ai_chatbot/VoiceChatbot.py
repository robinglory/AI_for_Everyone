import customtkinter as ctk
import google.generativeai as genai
import speech_recognition as sr
from gtts import gTTS
from threading import Thread
import os
import pyttsx3
import pygame
import time

# Configure Gemini API
genai.configure(api_key="AIzaSyDo01CBIaanACl5voE9NEm7CdjtFPp6P2c")


# Initialize the speech engine
engine = pyttsx3.init()

# Global flag to track if the engine is busy
is_speaking = False 

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

# Convert text to speech
# def speak(text):
#     tts = gTTS(text=text, lang="en")
#     tts.save("response.mp3")
#     pygame.mixer.init()
#     pygame.mixer.music.load("response.mp3")
#     pygame.mixer.music.play()



def speak(text):
    if not text.strip():
        return  # Don't try to speak empty responses

    try:
        engine.setProperty('rate', 200)  # Set the speed (lower is slower)
        engine.setProperty('volume', 1)  # Set volume (0.0 to 1.0)
        engine.say(text)
        engine.runAndWait()  # Immediately process the speech without delay
    except Exception as e:
        print("Error in voice output:", e)

# Listen for voice input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        chat_display.insert("end", "🎤 Listening...\n", "bot")
        chat_display.yview("end")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand."
        except sr.RequestError:
            return "Could not request results, please check your connection."

# Handle chatbot response
def chatbot_response(user_input):
    if not user_input:
        return

    chat_display.insert("end", f"🧑‍💻 You: {user_input}\n\n", "user")
    chat_display.insert("end", "🤖 Chatbot: Thinking...\n", "bot")
    chat_display.yview("end")

    def generate_response():
        response = get_gemini_response(user_input, pdf_text)
        chat_display.delete("end-2l", "end")  # Remove "Thinking..."
        chat_display.insert("end", f"🤖 Chatbot: {response}\n\n", "bot")
        chat_display.yview("end")
        
        # Run speech in a separate thread to avoid blocking
        Thread(target=speak, args=(response,)).start()

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
