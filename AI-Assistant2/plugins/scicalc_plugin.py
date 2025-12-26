import math

allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
allowed_names.update({"abs": abs, "round": round})

def can_handle(text: str) -> bool:
    return text.strip().lower().startswith("sci ")

def handle(text: str) -> str:
    expression = text.strip()[4:]  # remove 'sci '
    try:
        result = eval(expression, {"__builtins__": None}, allowed_names)
        return f"🧪 Scientific Result: {result}"
    except Exception as e:
        return f"❌ Invalid expression: {e}"
