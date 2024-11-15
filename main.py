from src.calculator import Calculator
from src.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from src.history_manager import HistoryFacade
from src.logger import logger
from src.plugin_manager import PluginManager
from src.plugins.power_plugin import PowerPlugin  # Example of a plugin to calculate power

def run():
    calculator = Calculator()
    history_facade = HistoryFacade()
    plugin_manager = PluginManager()
    plugin_manager.register_plugin("power", PowerPlugin())

    command_dict = initialize_commands(calculator, history_facade, plugin_manager)
    show_commands(command_dict)

    while True:
        command_input = input(">> ").strip().lower()
        if is_exit_command(command_input):
            break

        command_name, args = parse_command(command_input, command_dict)
        if not command_name:
            print("Unknown command")
            show_commands(command_dict)
            continue

        handle_command(command_name, args, command_dict, history_facade)


def initialize_commands(calculator, history_facade, plugin_manager):
    # Core calculator commands
    add_command = AddCommand(calculator, history_facade)
    subtract_command = SubtractCommand(calculator, history_facade)
    multiply_command = MultiplyCommand(calculator, history_facade)
    divide_command = DivideCommand(calculator, history_facade)

    # Command dictionary
    command_dict = {
        "add": add_command,
        "subtract": subtract_command,
        "multiply": multiply_command,
        "divide": divide_command,
        "load_history": 'load_history',
        "clear_history": 'clear_history'
    }

    # Include plugin commands
    for plugin_name in plugin_manager.list_plugins():
        command_dict[plugin_name] = plugin_manager.get_plugin(plugin_name)
    
    return command_dict


def show_commands(command_dict):
    print("Available commands:")
    for command in command_dict:
        if command in ['load_history', 'clear_history']:
            print(f">> {command} --> {command}")
        else:
            print(f">> {command} --> {command} num1 num2 (or other required arguments)")


def is_exit_command(command_input):
    return command_input in ["exit", "q", "quit", "Q"]


def parse_command(command_input, command_dict):
    if command_input.isdigit():
        command_index = int(command_input) - 1
        if 0 <= command_index < len(command_dict):
            command_name = list(command_dict.keys())[command_index]
        else:
            print("Invalid command number.")
            return None, []
    else:
        parts = command_input.split()
        command_name = parts[0]
        args = parse_arguments(parts[1:])
    
    return command_name if command_name in command_dict else None, args


def parse_arguments(arg_strings):
    try:
        return list(map(float, arg_strings))
    except ValueError:
        print("Invalid arguments. Please provide numbers.")
        return []


def handle_command(command_name, args, command_dict, history_facade):
    try:
        if command_name == "load_history":
            handle_load_history(history_facade)
        elif command_name == "clear_history":
            handle_clear_history(history_facade)
        else:
            execute_command(command_name, args, command_dict)
    except Exception as e:
        logger.error(f"Error: {e}")


def handle_load_history(history_facade):
    try:
        load_history = history_facade.load_history()
        print(load_history)
        logger.info("History loaded successfully")
    except Exception:
        print("No data found")
        logger.info("No data found when history loaded...")


def handle_clear_history(history_facade):
    history_facade.clear_history()
    logger.info("History cleared successfully")
    print("History cleared successfully")


def execute_command(command_name, args, command_dict):
    command = command_dict[command_name]
    if isinstance(command, (AddCommand, SubtractCommand, MultiplyCommand, DivideCommand)):
        result = command.execute(*args)
        print(f"Result: {result}")
        logger.info(f"Result of {command_name} with value {args} is {result}")
    else:
        result = command.execute(*args)
        print(f"Plugin Result: {result}")
        logger.info(f"Result of {command_name} plugin with arguments {args}: {result}")


if __name__ == "__main__":
    run()
