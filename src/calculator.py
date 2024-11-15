class Calculator:
    def add(self, *args):
        """Performs addition of two numbers."""
        return sum(args)

    def subtract(self, x, y):
        """Performs subtraction of two numbers."""
        return x - y

    def multiply(self, *args):
        if len(args) == 0:
            raise ValueError("At least one number is required for multiplication.")
        result = 1
        for number in args:
            result *= number
        return result

    def divide(self, *args):
        if len(args) == 0:
            raise ValueError("At least two number is required for division.")
        if len(args) == 1:
            raise ValueError("At least two number is required for division.")
        if 0 in args[1:]:
            raise ValueError("Division by zero is not allowed.")
        result = args[0]
        for number in args[1:]:
            result /= number
        return result





