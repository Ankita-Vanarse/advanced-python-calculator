from src.plugins.plugin_interface import PluginInterface

class PowerPlugin(PluginInterface):
    def execute(self, base, exponent):
        return base ** exponent
