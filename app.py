import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("Chat with gemini! Type 'exit' to quit.")
while True:
	user_input = input("You: ")
	if user_input == "exit":
		break
	response = chat.send_message(user_input)
	print("Gemini:", response.text)