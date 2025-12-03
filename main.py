from fastapi import FastAPI
from fastapi import HTTPException
from models import ChatRequest, ChatResponse
from chat_service import generate_reply

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status":"ok"}

@app.post("/chat", response_model=ChatResponse)
def handle_chat(request:ChatRequest):
    try:
        reply,model= generate_reply(request.message)
        return {"reply": reply, "model": model}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/upload")
def upload_file():
    return {"status":"not implemented yet."}

@app.post("/ask")
def ask_question():
    return {"status":"not implemented yet."}

