def route_command(user_input: str, plugins: dict) -> str:
    for name, plugin in plugins.items():
        if hasattr(plugin, "can_handle") and plugin.can_handle(user_input):
            return plugin.handle(user_input)
    return None  # fallback to LLM


if __name__=='__main__':
    pass
