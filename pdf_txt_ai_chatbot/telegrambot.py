import logging
import google.generativeai as genai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# 🔹 Configure Gemini API
GENAI_API_KEY = "AIzaSyDo01CBIaanACl5voE9NEm7CdjtFPp6P2c"
genai.configure(api_key=GENAI_API_KEY)

# 🔹 Configure Telegram Bot Token
TELEGRAM_BOT_TOKEN = "7557629223:AAG9bvuDOz_NoKx1_7R_cpYw4Tze2Gc6WFM"

# 🔹 Enable Logging (Optional)
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s",
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# 🔹 Load Extracted Text from File
def load_text(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: PDF text file not found."

# 🔹 Set File Path for Context (Update This Path)
pdf_text = load_text(r"C:\Users\ASUS\Documents\Python\Programs\pdf_txt_ai_chatbot\amecal_txt.txt")

# 🔹 Function to Get AI Response
def get_gemini_response(query, context):
    prompt = f"Based on the following document:\n\n{context}\n\nAnswer the question: {query}"

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# 🔹 Command: Start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("🤖 Hello! I am your AI chatbot. Send me a question, and I'll answer based on my knowledge!")

# 🔹 Command: Help
async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("💡 Just type your question, and I'll respond!")

# 🔹 Handle Messages (AI Responses)
async def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    response = get_gemini_response(user_message, pdf_text)
    await update.message.reply_text(response)

# 🔹 Main Function to Run the Bot
def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    print("🤖 Bot is running...")
    app.run_polling()

# Run the bot
if __name__ == "__main__":
    main()
