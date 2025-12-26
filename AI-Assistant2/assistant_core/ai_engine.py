import os
from dotenv import load_dotenv
import openai

load_dotenv()

MODEL = os.getenv("OLLAMA_MODEL", "tinyllama")
SERVER = os.getenv("OLLAMA_SERVER", "http://localhost:11434")

openai.api_base = f"{SERVER}/v1"
openai.api_key = "ollama"  # dummy key required even for local Ollama

def generate_response(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response.choices[0].message["content"].strip()
