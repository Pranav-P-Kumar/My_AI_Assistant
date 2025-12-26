import os
import importlib.util

def load_plugins(plugin_dir="plugins"):
    plugins = {}
    for fname in os.listdir(plugin_dir):
        if fname.endswith(".py"):
            name = fname[:-3]
            spec = importlib.util.spec_from_file_location(name, os.path.join(plugin_dir, fname))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            plugins[name] = module
    return plugins
