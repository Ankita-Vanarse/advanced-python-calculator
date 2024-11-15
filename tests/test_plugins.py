import pytest
from src.plugin_manager import PluginManager
from src.plugins.plugin_interface import PluginInterface



class TestPlugin(PluginInterface):
    def execute(self, *args):
        return "Plugin executed successfully"

class PowerPlugin(PluginInterface):
    def execute(self, base, exponent):
        return base ** exponent


@pytest.fixture
def plugin_manager():
    return PluginManager()


def test_register_and_retrieve_plugin(plugin_manager):
    plugin = TestPlugin()
    plugin_manager.register_plugin("test_plugin", plugin)
    
    retrieved_plugin = plugin_manager.get_plugin("test_plugin")
    assert retrieved_plugin is not None
    assert isinstance(retrieved_plugin, PluginInterface)
    assert retrieved_plugin.execute() == "Plugin executed successfully"


def test_power_plugin(plugin_manager):
    plugin = PowerPlugin()
    plugin_manager.register_plugin("power", plugin)
    
    power_plugin = plugin_manager.get_plugin("power")
    result = power_plugin.execute(2, 3)
    print(result)
    assert power_plugin is not None
    assert isinstance(power_plugin, PluginInterface)
    assert result == 8