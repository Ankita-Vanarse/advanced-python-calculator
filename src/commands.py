class Command:
    def execute(self, *args):
        raise NotImplementedError("Command must implement 'execute'")

class AddCommand(Command):
    def __init__(self, calculator, history_facade):
        self.calculator = calculator
        self.history_facade = history_facade

    def execute(self, *args):
        result = self.calculator.add(*args)
        self.history_facade.save_calculation("add", list(args), result)
        return result

class SubtractCommand(Command):
    def __init__(self, calculator, history_facade):
        self.calculator = calculator
        self.history_facade = history_facade

    def execute(self, x, y):
        result = self.calculator.subtract(x, y)
        self.history_facade.save_calculation("subtract", [x, y], result)
        return result


class MultiplyCommand(Command):
    def __init__(self, calculator, history_facade):
        self.calculator = calculator
        self.history_facade = history_facade

    def execute(self, *args):
        result = self.calculator.multiply(*args)
        self.history_facade.save_calculation("multiply", list(args), result)
        return result
    

class DivideCommand(Command):
    def __init__(self, calculator, history_facade):
        self.calculator = calculator
        self.history_facade = history_facade

    def execute(self, *args):
        result = self.calculator.divide(*args)
        self.history_facade.save_calculation("divide", list(args), result)
        return result