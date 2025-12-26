from assistant_core.ai_engine import generate_response
from assistant_core.plugin_loader import load_plugins
from assistant_core.command_router import route_command
from ui.terminal_chat import chat_loop

plugins = load_plugins()

def get_response(user_input: str) -> str:
    plugin_resp = route_command(user_input, plugins)
    if plugin_resp:
        return plugin_resp
    return generate_response(user_input)

from ui.gui_chat import GUIChat

if __name__ == "__main__":
    gui = GUIChat(get_response)
    gui.run()

