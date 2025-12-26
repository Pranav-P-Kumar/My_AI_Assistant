# plugins/quiz_plugin.py

import random

questions = [
    {"q": "What is the capital of France?", "a": "Paris"},
    {"q": "2 + 2 * 3?", "a": "8"},
    {"q": "Who wrote 'To Kill a Mockingbird'?", "a": "Harper Lee"},
]

last_question = None
last_answer = None

def can_handle(text: str) -> bool:
    return text.strip().lower().startswith("quiz me")

def handle(text: str) -> str:
    global last_question, last_answer
    qa = random.choice(questions)
    last_question, last_answer = qa["q"], qa["a"]
    return f"❓ Question: {qa['q']}\n(Reply with 'answer: <your answer>')"
