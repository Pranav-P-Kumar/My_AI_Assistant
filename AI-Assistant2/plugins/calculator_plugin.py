def can_handle(text: str) -> bool:
    return text.strip().lower().startswith("calc")      # To use start with 'calc'

def handle(text: str) -> str:
    try:
        expression = text.strip()[5:]  # remove 'calc '
        result = eval(expression, {"__builtins__": None}, {})
        return f"🧮 Result: {result}"
    except Exception as e:
        return f"❌ Error in calculation: {e}"
