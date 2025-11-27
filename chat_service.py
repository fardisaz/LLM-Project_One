from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_reply(message:str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=message)
    return response.text, "gemini-2.5-flash"