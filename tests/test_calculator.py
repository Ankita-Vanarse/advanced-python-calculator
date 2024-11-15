import pytest, os, sys
from src.calculator import Calculator
from src.commands import *
from src.history_manager import HistoryFacade

@pytest.fixture
def setup():
    # Initialize the Calculator and HistoryFacade for testing
    calculator = Calculator()
    history_facade = HistoryFacade()
    history_facade.history_file = "./data/test_calculation_history.csv"

    # Ensure the file is clean before testing
    if os.path.exists(history_facade.history_file):
        open(history_facade.history_file, 'w').close()

    with open(history_facade.history_file, 'w') as f:
        f.write("Operation,Data,Result\n")

    return calculator, history_facade

def test_add_command(setup):
    calculator, history_facade = setup
    add_command = AddCommand(calculator, history_facade)

    result = add_command.execute(10, 5)
    assert result == 15

    # Verify history is saved correctly
    data = history_facade.load_history()
    assert len(data) == 1
    print(data)
    assert data.iloc[0]["Operation"] == "add"
    assert data.iloc[0]["Result"] == 15

def test_subtract_command(setup):
    calculator, history_facade = setup
    subtract_command = SubtractCommand(calculator, history_facade)

    result = subtract_command.execute(10, 5)
    assert result == 5

    # Verify history is saved correctly
    data = history_facade.load_history()
    assert len(data) == 1
    assert data.iloc[0]["Operation"] == "subtract"
    assert data.iloc[0]["Result"] == 5

def test_divide_by_zero(setup):
    calculator, _ = setup

    with pytest.raises(ValueError) as e:
        calculator.divide(10, 0)
    
    assert str(e.value) == "Division by zero is not allowed."

def test_multiply(setup):
    calculator, history_facade = setup
    multiply_command = MultiplyCommand(calculator, history_facade)
    result = multiply_command.execute(3, 7)
    print(result)
    assert result == 21

    # Verify history is saved correctly
    data = history_facade.load_history()
    print(data)
    assert len(data) == 1
    assert data.iloc[0]["Operation"] == "multiply"
    assert data.iloc[0]["Result"] == 21
