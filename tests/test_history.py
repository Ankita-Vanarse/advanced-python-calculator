import os
import pandas as pd
import pytest
from src.history_manager import HistoryFacade

@pytest.fixture
def history_manager():
    history_facade = HistoryFacade()
    history_facade.history_file = "./data/test_calculation_history.csv"

    # Ensure the file is clean before testing
    if os.path.exists(history_facade.history_file):
        open(history_facade.history_file, 'w').close()

    with open(history_facade.history_file, 'w') as f:
        f.write("Operation,Data,Result\n")

    return history_facade


def test_save_and_load(history_manager):
    # Save a calculation using Singleton history manager
    history_manager.save_calculation("add", [5, 3], 8)
    
    # Check if the saved calculation exists
    data = history_manager.load_history()
    assert len(data) == 1
    assert data.iloc[0]["Operation"] == "add"
    assert data.iloc[0]["Result"] == 8

def test_simplified_methods(history_manager):
    # Save and check using facade methods
    history_manager.save_calculation("multiply", [2, 4, 2], 16)
    data = history_manager.load_history()
    assert len(data) == 1
    assert data.iloc[0]["Operation"] == "multiply"
    assert data.iloc[0]["Result"] == 16
    
    # Clear the history
    history_manager.clear_history()
    assert os.path.exists(history_manager.history_file)
