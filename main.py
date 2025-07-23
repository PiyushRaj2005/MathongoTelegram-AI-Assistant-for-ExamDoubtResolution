from telegram import Update 
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from utils.fetch_links import get_links
from prompts.fallback import get_fallback_response
from tts.speak import generate_audio

import json
import requests
import os

# --- Configuration ---
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3"  # Make sure it's pulled using `ollama pull llama3`
BOT_TOKEN = "8037454716:AAHqwZ_-HicPCauGJMva3qUaxwC89WlvJTg"  # Replace if needed

# --- Command Handlers ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! I’m your JEE/NEET assistant.\nAsk any doubt or try /pattern, /syllabus, /formdeadline."
    )

async def handle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cmd = update.message.text.strip().lower()
    command_responses = {
        "/pattern": "📘 *JEE Pattern*: 2 papers (PCM), each 3 hours. Includes MCQs and numerical type questions.",
        "/syllabus": "📚 *Syllabus*: NCERT 11th + 12th topics for Physics, Chemistry, and Maths/Biology.",
        "/formdeadline": "📅 *Form Deadlines*: JEE forms usually come in Dec–Jan. NEET forms in Feb–March. Check nta.ac.in."
    }

    response = command_responses.get(cmd, "Unknown command. Try /pattern, /syllabus, or /formdeadline.")
    from telegram.helpers import escape_markdown

    safe_response = escape_markdown(response, version=2)
    await update.message.reply_text(safe_response, parse_mode="MarkdownV2")


# --- Main AI Message Handler ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from telegram.helpers import escape_markdown

    user_input = update.message.text.strip().lower()

    # 1. Try Ollama
    response = call_ollama(user_input)

    # 2. If Ollama fails, fallback
    if not response:
        response = get_fallback_response(user_input)

    # 3. Relevant links
    links = get_links(user_input)
    if links:
        response += "\n\n🔗 *Relevant Resources*:\n" + "\n".join(links)

    # 4. Escape special Markdown characters
    safe_response = escape_markdown(response, version=2)

    # 5. Text reply (escaped)
    await update.message.reply_text(safe_response, parse_mode="MarkdownV2")

    # 6. Audio reply (plain text, no escaping needed here)
    audio_path = generate_audio(response)
    if audio_path and os.path.exists(audio_path):
        with open(audio_path, 'rb') as audio_file:
            await update.message.reply_voice(voice=audio_file)



# --- Ollama Call ---
def call_ollama(prompt: str):
    try:
        res = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": f"Answer this clearly for a JEE/NEET student in Hinglish or English: {prompt}",
                "stream": True
            },
            stream=True
        )

        full_response = ""
        for line in res.iter_lines():
            if line:
                try:
                    json_data = json.loads(line.decode("utf-8"))
                    full_response += json_data.get("response", "")
                except Exception as parse_err:
                    print("Line parse error:", parse_err)

        return full_response.strip()

    except Exception as e:
        print(f"Ollama call failed: {e}")
        return None

# --- Run Bot ---
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler(["pattern", "syllabus", "formdeadline"], handle_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()
