##NOT working

import customtkinter as ctk
import requests  # For making API requests to DeepSeek
import speech_recognition as sr
import pygame
from gtts import gTTS
from threading import Thread
import os
from googletrans import Translator


class ChatbotApp:
    def __init__(self, api_key, text_file_path):
        self.api_key = "sk-609cb552cfbe469bbd7f1fc5689e6a9da" # DeepSeek API key
        self.translator = Translator()  # Initialize translator
        self.pdf_text = self.load_text(text_file_path)  # Load PDF text
        self.setup_gui()  # Initialize GUI

    # Load extracted text from file
    def load_text(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return "Error: PDF text file not found."

    # Generate AI response using DeepSeek API
    def get_deepseek_response(self, query, context):
        prompt = f"Based on the following document:\n\n{context}\n\nAnswer in Burmese: {query}"
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",  # Use your DeepSeek API key
                "Content-Type": "application/json",
            }
            data = {
                "prompt": prompt,
                "max_tokens": 150,  # Adjust as needed
                "temperature": 0.7,  # Adjust for creativity
            }
            response = requests.post(
                "https://api.deepseek.com/v1/chat/completions",  # DeepSeek API endpoint
                headers=headers,
                json=data,
            )
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()["choices"][0]["text"].strip()  # Extract response text
        except Exception as e:
            return f"Error: {e}"

    # Convert text to speech (Burmese)
    def speak(self, text):
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
    def listen(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.chat_display.insert("end", "🎤 Listening...\n", "bot")
            self.chat_display.yview("end")
            try:
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio, language="my")  # Use Burmese language
                return text
            except sr.UnknownValueError:
                return "မဖတ်နိုင်ပါ"
            except sr.RequestError:
                return "Could not request results, please check your connection."

    # Handle chatbot response with language detection
    def chatbot_response(self, user_input):
        if not user_input:
            return

        # Detect input language (Burmese or English)
        detected_lang = self.translator.detect(user_input).lang

        # Insert the user's message in the chat window
        self.chat_display.insert("end", f"🧑‍💻 You: {user_input}\n\n", "user")
        self.chat_display.insert("end", "🤖 Chatbot: Thinking...\n", "bot")
        self.chat_display.yview("end")

        def generate_response():
            response = None

            # Check if the input exists in the PDF text (if found, return it)
            if user_input in self.pdf_text:
                response = user_input  # Return the exact input text if found

            # If the input is not found in the text file, ask DeepSeek
            if not response:
                response = self.get_deepseek_response(user_input, self.pdf_text)

            # If the detected language is English, return response in English
            if detected_lang == "en":
                response_final = response  # Keep in English

            # If the detected language is Burmese, return response in Burmese (no translation)
            elif detected_lang == "my":
                response_final = response  # Keep in Burmese

            else:
                # Default to English if language can't be detected
                response_final = response

            # Remove "Thinking..." from the chat display
            self.chat_display.delete("end-2l", "end")

            # Display the chatbot response
            self.chat_display.insert("end", f"🤖 Chatbot: {response_final}\n\n", "bot")
            self.chat_display.yview("end")

            # Speak the response in the detected language
            self.speak(response_final)

        Thread(target=generate_response).start()

    # Function to handle voice input
    def voice_input(self):
        user_input = self.listen()
        self.user_entry.delete(0, "end")
        self.user_entry.insert(0, user_input)  # Show recognized text in input field
        self.chatbot_response(user_input)

    # Function to send text input
    def text_input(self):
        user_input = self.user_entry.get().strip()
        self.user_entry.delete(0, "end")
        self.chatbot_response(user_input)

    # Function to clear chat
    def clear_chat(self):
        self.chat_display.delete("1.0", "end")

    # Setup GUI
    def setup_gui(self):
        ctk.set_appearance_mode("dark")  # Dark Mode
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("AI Chatbot with Voice (DeepSeek)")
        self.root.geometry("600x700")

        # Chat Display Area
        self.chat_display = ctk.CTkTextbox(self.root, width=550, height=500, wrap="word", font=("Arial", 14))
        self.chat_display.pack(pady=10)
        self.chat_display.tag_config("user", foreground="cyan")
        self.chat_display.tag_config("bot", foreground="lightgreen")

        # User Input Field
        self.user_entry = ctk.CTkEntry(self.root, width=400, font=("Arial", 14))
        self.user_entry.pack(pady=5)

        # Button Frame
        button_frame = ctk.CTkFrame(self.root)
        button_frame.pack(pady=5)

        # Send Button
        send_button = ctk.CTkButton(button_frame, text="Send", command=self.text_input, font=("Arial", 14), corner_radius=10)
        send_button.grid(row=0, column=0, padx=5)

        # Voice Button
        voice_button = ctk.CTkButton(button_frame, text="🎤 Speak", command=self.voice_input, font=("Arial", 14), corner_radius=10)
        voice_button.grid(row=0, column=1, padx=5)

        # Clear Chat Button
        clear_button = ctk.CTkButton(self.root, text="Clear Chat", command=self.clear_chat, font=("Arial", 14), corner_radius=10)
        clear_button.pack(pady=5)

        # Bind "Enter" Key to Send Message
        def enter_key(event):
            self.text_input()

        self.root.bind("<Return>", enter_key)

    # Run the application
    def run(self):
        self.root.mainloop()


# Main entry point
if __name__ == "__main__":
    # Configure API key and text file path
    API_KEY = "sk-609cb552cfbe469bbd7f1fc5689e6a9da"  # Replace with your DeepSeek API key
    TEXT_FILE_PATH = r"C:\Users\ASUS\Documents\Python\Programs\pdf_txt_ai_chatbot\test.txt"  # Replace with your text file path

    # Create and run the chatbot app
    chatbot_app = ChatbotApp(API_KEY, TEXT_FILE_PATH)
    chatbot_app.run()