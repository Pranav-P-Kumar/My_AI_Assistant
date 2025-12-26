# plugins/answer_plugin.py

import sys
import importlib

sys.path.insert(0, 'C:\\Work\\Projects\\AI-Assistant2')
# Dynamically get quiz_plugin from the plugin directory
quiz_plugin = importlib.import_module("plugins.quiz_plugin")

def can_handle(text: str) -> bool:
    return text.strip().lower().startswith("answer:")

def handle(text: str) -> str:
    answer = text.partition(":")[2].strip()
    if not quiz_plugin.last_answer:
        return "🤔 I haven't asked a quiz question yet. Type 'quiz me'."
    correct = quiz_plugin.last_answer.strip().lower()
    return "✅ Correct!" if answer.strip().lower() == correct else f"❌ Wrong. Correct answer: {quiz_plugin.last_answer}"


if __name__=='__main__':
    print(quiz_plugin)
    print(quiz_plugin.last_answer)