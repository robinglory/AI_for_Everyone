# import customtkinter as ctk
# import google.generativeai as genai
# import speech_recognition as sr
# import pygame
# from gtts import gTTS
# from threading import Thread
# import os
# from googletrans import Translator

# # Configure Gemini API
# genai.configure(api_key="AIzaSyBRG35ZZwUDaO7Hi8VI4GTCD6AjuUW6xoI")

# # Initialize Translator for Burmese
# translator = Translator()

# # Load extracted text from file
# def load_text(file_path):
#     try:
#         with open(file_path, "r", encoding="utf-8") as file:
#             return file.read()
#     except FileNotFoundError:
#         return "Error: PDF text file not found."

# # Generate AI response using Gemini
# def get_gemini_response(query, context):
#     prompt = f"Based on the following document:\n\n{context}\n\nAnswer in Burmese: {query}"
#     try:
#         model = genai.GenerativeModel("gemini-pro")
#         response = model.generate_content(prompt)
#         return response.text  # Extract response text
#     except Exception as e:
#         return f"Error: {e}"

# # Convert text to speech (Burmese)
# def speak(text):
#     if not text.strip():
#         return  # Don't try to speak empty responses

#     try:
#         tts = gTTS(text=text, lang="my")
#         audio_file = "response.mp3"
#         tts.save(audio_file)

#         # Reinitialize pygame each time to prevent audio issues
#         pygame.mixer.init()
#         pygame.mixer.music.load(audio_file)
#         pygame.mixer.music.play()

#         # Wait for the audio to finish playing
#         while pygame.mixer.music.get_busy():
#             pygame.time.Clock().tick(10)

#         # Stop the mixer and unload the file
#         pygame.mixer.music.stop()
#         pygame.mixer.quit()

#         # Wait a short moment to ensure file is released
#         pygame.time.delay(100)

#         # Delete the file safely
#         if os.path.exists(audio_file):
#             os.remove(audio_file)
#     except Exception as e:
#         print("Error in voice output:", e)

# # Listen for voice input (Burmese)
# def listen():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         chat_display.insert("end", "🎤 Listening...\n", "bot")
#         chat_display.yview("end")
#         try:
#             audio = recognizer.listen(source, timeout=5)
#             text = recognizer.recognize_google(audio, language="my")  # Use Burmese language
#             return text
#         except sr.UnknownValueError:
#             return "မဖတ်နိုင်ပါ"
#         except sr.RequestError:
#             return "Could not request results, please check your connection."

# # Handle chatbot response with language detection
# # Handle chatbot response with language detection
# def chatbot_response(user_input):
#     if not user_input:
#         return

#     # Detect input language (Burmese or English)
#     detected_lang = translator.detect(user_input).lang

#     # Insert the user's message in the chat window
#     chat_display.insert("end", f"🧑‍💻 You: {user_input}\n\n", "user")
#     chat_display.insert("end", "🤖 Chatbot: Thinking...\n", "bot")
#     chat_display.yview("end")

#     def generate_response():
#         response = None

#         # Check if the input exists in the PDF text (if found, return it)
#         if user_input in pdf_text:
#             response = user_input  # Return the exact input text if found

#         # If the input is not found in the text file, ask Gemini
#         if not response:
#             response = get_gemini_response(user_input, pdf_text)

#         # If the detected language is English, return response in English
#         if detected_lang == "en":
#             response_final = response  # Keep in English

#         # If the detected language is Burmese, return response in Burmese (no translation)
#         elif detected_lang == "my":
#             response_final = response  # Keep in Burmese

#         else:
#             # Default to English if language can't be detected
#             response_final = response

#         # Remove "Thinking..." from the chat display
#         chat_display.delete("end-2l", "end")  

#         # Display the chatbot response
#         chat_display.insert("end", f"🤖 Chatbot: {response_final}\n\n", "bot")
#         chat_display.yview("end")

#         # Speak the response in the detected language
#         speak(response_final)  

#     Thread(target=generate_response).start()

# # Function to handle voice input
# def voice_input():
#     user_input = listen()
#     user_entry.delete(0, "end")
#     user_entry.insert(0, user_input)  # Show recognized text in input field
#     chatbot_response(user_input)

# # Function to send text input
# def text_input():
#     user_input = user_entry.get().strip()
#     user_entry.delete(0, "end")
#     chatbot_response(user_input)

# # Function to clear chat
# def clear_chat():
#     chat_display.delete("1.0", "end")

# # Load PDF text
# pdf_text = load_text(r"C:\Users\ASUS\Documents\Python\Programs\OCR Python\captured_text.txt")

# # Create GUI Window
# ctk.set_appearance_mode("dark")  # Dark Mode    
# ctk.set_default_color_theme("blue")

# root = ctk.CTk()
# root.title("AI Chatbot with Voice (Gemini)")
# root.geometry("600x700")

# # Chat Display Area
# chat_display = ctk.CTkTextbox(root, width=550, height=500, wrap="word", font=("Arial", 14))
# chat_display.pack(pady=10)
# chat_display.tag_config("user", foreground="cyan")
# chat_display.tag_config("bot", foreground="lightgreen")

# # User Input Field
# user_entry = ctk.CTkEntry(root, width=400, font=("Arial", 14))
# user_entry.pack(pady=5)

# # Button Frame
# button_frame = ctk.CTkFrame(root)
# button_frame.pack(pady=5)

# # Send Button
# send_button = ctk.CTkButton(button_frame, text="Send", command=text_input, font=("Arial", 14), corner_radius=10)
# send_button.grid(row=0, column=0, padx=5)

# # Voice Button
# voice_button = ctk.CTkButton(button_frame, text="🎤 Speak", command=voice_input, font=("Arial", 14), corner_radius=10)
# voice_button.grid(row=0, column=1, padx=5)

# # Clear Chat Button
# clear_button = ctk.CTkButton(root, text="Clear Chat", command=clear_chat, font=("Arial", 14), corner_radius=10)
# clear_button.pack(pady=5)

# # Bind "Enter" Key to Send Message
# def enter_key(event):
#     text_input()

# root.bind("<Return>", enter_key)

# # Run GUI
# root.mainloop()


##Deepseek

import customtkinter as ctk
import google.generativeai as genai
from threading import Thread
from gtts import gTTS
import os
import langdetect
from langdetect import detect

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
    # Detect language of the query
    try:
        lang = detect(query)
    except:
        lang = "en"  # Default to English if detection fails

    prompt = f"Based on the following document:\n\n{context}\n\nAnswer the question: {query}"
    if lang == "my":  # If the question is in Burmese
        prompt = f"အောက်ပါစာတမ်းကိုအခြေခံပြီး:\n\n{context}\n\nမေးခွန်းကိုဖြေပါ: {query}"

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text  # Extract response text
    except Exception as e:
        return f"Error: {e}"

# Function to convert text to speech
def text_to_speech(text, lang="en"):
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save("output.mp3")
        os.system("start output.mp3")  # Play the audio (Windows)
    except Exception as e:
        print(f"Error in TTS: {e}")

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

        # Convert chatbot response to speech
        try:
            lang = detect(user_input)  # Detect language of user input
            if lang == "my":
                text_to_speech(response, lang="my")  # Burmese TTS
            else:
                text_to_speech(response, lang="en")  # English TTS
        except:
            text_to_speech(response, lang="en")  # Default to English

    Thread(target=generate_response).start()

# Function to speak user input
def speak_user_input():
    user_input = user_entry.get().strip()
    if user_input:
        try:
            lang = detect(user_input)  # Detect language of user input
            if lang == "my":
                text_to_speech(user_input, lang="my")  # Burmese TTS
            else:
                text_to_speech(user_input, lang="en")  # English TTS
        except:
            text_to_speech(user_input, lang="en")  # Default to English

# Function to clear chat
def clear_chat():
    chat_display.delete("1.0", "end")

# Load PDF text
pdf_text = load_text(r"C:\Users\ASUS\Documents\Python\Programs\OCR Python\captured_text.txt")

# Create GUI Window
ctk.set_appearance_mode("dark")  # Dark Mode
ctk.set_default_color_theme("green")  # Modern theme

root = ctk.CTk()
root.title("Advanced AI Chatbot (Gemini)")
root.geometry("700x800")

# Chat Display Area
chat_display = ctk.CTkTextbox(root, width=650, height=550, wrap="word", font=("Arial", 14))
chat_display.pack(pady=10, padx=10)
chat_display.tag_config("user", foreground="cyan")
chat_display.tag_config("bot", foreground="lightgreen")

# User Input Frame
input_frame = ctk.CTkFrame(root)
input_frame.pack(pady=10, padx=10, fill="x")

# User Input Field
user_entry = ctk.CTkEntry(input_frame, width=450, font=("Arial", 14))
user_entry.pack(pady=5, padx=5, side="left", expand=True, fill="x")

# Speak User Input Button
speak_user_button = ctk.CTkButton(input_frame, text="Speak", command=speak_user_input, font=("Arial", 14), width=50)
speak_user_button.pack(pady=5, padx=5, side="left")

# Send Button
send_button = ctk.CTkButton(input_frame, text="Send", command=chatbot_response, font=("Arial", 14), width=50)
send_button.pack(pady=5, padx=5, side="left")

# Clear Chat Button
clear_button = ctk.CTkButton(root, text="Clear Chat", command=clear_chat, font=("Arial", 14), corner_radius=10)
clear_button.pack(pady=5)

# Bind "Enter" Key to Send Message
def enter_key(event):
    chatbot_response()

root.bind("<Return>", enter_key)

# Run GUI
root.mainloop()