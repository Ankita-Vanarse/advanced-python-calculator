from src.plugins.plugin_interface import PluginInterface

class PluginManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PluginManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.plugins = {}
        return cls._instance

    def register_plugin(self, name, plugin: PluginInterface):
        """Register a new plugin."""
        self.plugins[name] = plugin

    def get_plugin(self, name):
        """Retrieve a registered plugin."""
        return self.plugins.get(name, None)

    def list_plugins(self):
        """List all available plugins."""
        return self.plugins.keys()
