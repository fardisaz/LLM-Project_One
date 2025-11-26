from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class ChatRequest(BaseModel):
    message:str

class ChatResponse(BaseModel):
    reply:str
    model:str

@app.get("/health")
def health_check():
    return {"status":"ok"}


@app.post("/chat", response_model=ChatResponse)
def handle_chat(request:ChatRequest):
    try:
        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=request.message)
        response_model={
             "reply":response.text,
             "model":"gemini-2.5-flash"
         }
        return response_model
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




