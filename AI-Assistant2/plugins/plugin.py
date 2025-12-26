# Simple example: respond with current time
def can_handle(text: str) -> bool:
    return text.strip().lower() == "time"       # To use start with 'time'

def handle(text: str) -> str:
    from datetime import datetime
    return "Current time: " + datetime.now().strftime("%H:%M:%S")
