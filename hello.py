import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found")

client = genai.Client(api_key=api_key)

# Exactly one API request
response = client.interactions.create(
    model="gemini-3.6-flash",
    input="Hello! Introduce yourself in one sentence."
)

print(response.output_text)