from fastapi import APIRouter
from dotenv import load_dotenv
from pydantic import BaseModel
from llm_config import client, MODEL_NAME

load_dotenv(override=True)
router = APIRouter(prefix="/chat", tags=["AI Chat"])

SYSTEM_PROMPT = """
Eres un asistente útil que hace muchas referencias a canciones de rock de los 80´s.
"""

class Message(BaseModel):
    content: str
    role: str = "user"
    
class ChatRequest(BaseModel):
    messages: list[Message]
    
class ChatResponse(BaseModel):
    message: str

@router.post(
    "", # The path will be /chat
    summary="Generate a chat response using an LLM.",
    description=(
        "Generates a single response from a Large Language Model (LLM) based on the provided conversation history. "
        "This endpoint simulates an AI assistant who often makes references to 80s rock songs."
    ),
    response_description="The AI's generated message.",
    response_model=ChatResponse,
    status_code=200
)
async def chat_handler(chat_request: ChatRequest):
    respose = client.chat.completions.create(
        model = MODEL_NAME,
        temperature = 0.7,
        n = 1,
        messages = [{"role": "system", "content": SYSTEM_PROMPT}] + chat_request.messages,
    )

    return ChatResponse(message = respose.choices[0].message.content)