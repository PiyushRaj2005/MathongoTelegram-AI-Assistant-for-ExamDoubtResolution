# Telegram JEE/NEET AI Assistant 🤖

A prestigious, AI-powered Telegram bot designed to help students preparing for JEE and NEET exams. Get instant answers, official resources, and even voice responses in Hinglish or English—all in one place!

---

## ✨ Features

- **AI-Powered Q&A:** Uses [Ollama](https://ollama.com/) with the Llama 3 model for smart, context-aware answers.
- **Fallback Knowledge Base:** Reliable responses for common queries, even if AI is unavailable.
- **Relevant Resource Links:** Automatically fetches official links for forms, syllabus, patterns, and more.
- **Voice Replies:** Converts answers to audio (Hinglish/English) using Google Text-to-Speech.
- **Simple Commands:** `/pattern`, `/syllabus`, `/formdeadline` for quick info.

---

## 🚀 Getting Started
### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running locally
- Telegram bot token from [BotFather](https://core.telegram.org/bots#botfather)

---

### 2. Install Requirements

```sh
pip install -r requirements.txt
```

---

### 3. Set Up Ollama

Install Ollama and pull the Llama 3 model:

```sh
ollama pull llama3
```

Start the Ollama server:

```sh
ollama serve
```

---

### 4. Configure the Bot

Edit `main.py` and replace `BOT_TOKEN` with your Telegram bot token.

---

### 5. Run the Bot

```sh
python main.py
```
---

## 📝 Usage

- **Start:** `/start`
- **Ask Anything:** Type your JEE/NEET question in Hinglish or English.
- **Quick Commands:**
    - `/pattern` — Exam pattern
    - `/syllabus` — Syllabus details
    - `/formdeadline` — Form release dates

---

## 🗂️ Project Structure

```
TelegramAiBot/
├── main.py
├── requirements.txt
```
TelegramAiBot/
├── main.py
├── requirements.txt
├── README.md
├── prompts/
│   ├── fallback.json
│   ├── fallback.py
│   └── __pycache__/
├── tts/
│   ├── response.mp3
│   ├── speak.py
│   └── __pycache__/
├── utils/
│   ├── fetch_links.py
│   └── __pycache__/
├── venv/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   ├── .gitignore
│   └── pyvenv.cfg
└── ... (other files)
```
└── ... (other files)
```

---

## 🤝 Contributing

Pull requests and suggestions are welcome! Please open an issue first to discuss changes.

---

## 📜 License

This project is for educational purposes.

---

## 🙏 Acknowledgements

- [python-telegram-bot](https://python-telegram-bot.org/)
- [gTTS](https://pypi.org/project/gTTS/)
- [Ollama](https://ollama.com/)
