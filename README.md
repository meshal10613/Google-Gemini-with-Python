# Gemini Terminal Chatbot (Python)

A simple terminal-based chatbot powered by **Google Gemini**. This script allows you to chat with Gemini directly from your command line using Python.

---

### 🚀 Features
- Real-time conversation with Gemini  
- Conversation history maintained automatically  
- Uses `.env` file for secure API key management  
- Easy to run and extend  

---

### 📦 Requirements
- Python 3.9+
- `google-generativeai`
- `python-dotenv`

---

### 🛠️ Installation

Clone the repository:
```bash
git clone https://github.com/meshal10613/Google-Gemini-with-Python

cd Google-Gemini-with-Python
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install google-generativeai python-dotenv
```
---

### 🔑 Environment Variables

Create a .env file in the project directory:
```env
GEMINI_API_KEY=your_api_key_here
```
Get your API key from Google AI Studio:
https://aistudio.google.com/

---

### ▶️ Run the Chatbot

```bash
python main.py
```

Expected output:
```bash
Chat with gemini! Type 'exit' to quit.
You:
```
---

### 📚 Notes

- You can swap "gemini-2.0-flash" with any other Gemini model.

- Do not commit your .env file or API key to GitHub.