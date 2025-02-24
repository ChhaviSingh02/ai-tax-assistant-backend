from fastapi import APIRouter
import openai
from config import OPENAI_API_KEY

router = APIRouter()

openai.api_key = OPENAI_API_KEY


@router.post("/chatbot")
def chatbot_response(query: str):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": query}]
    )
    return {"response": response['choices'][0]['message']['content']}
