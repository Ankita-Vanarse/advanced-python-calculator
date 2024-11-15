class PluginInterface:
    def execute(self, *args):
        raise NotImplementedError("Plugins must implement 'execute'")