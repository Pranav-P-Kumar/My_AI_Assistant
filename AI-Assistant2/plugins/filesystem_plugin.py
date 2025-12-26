import os

# to use filesystem plugin, the command has to start with either list files/ read file
def can_handle(text: str) -> bool:
    return text.strip().lower().startswith(("list files", "read file"))

def handle(text: str) -> str:
    try:
        cmd = text.strip().lower()
        if cmd.startswith("list files"):
            files = os.listdir(".")
            return "📂 Files:\n" + "\n".join(files)
        elif cmd.startswith("read file"):
            filename = cmd[len("read file "):].strip()
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read(500)
            return f"📖 Contents of {filename}:\n{content}"
    except Exception as e:
        return f"❌ File error: {e}"
