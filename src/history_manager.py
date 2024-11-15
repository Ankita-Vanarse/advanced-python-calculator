import pandas as pd
import os
import src.config as config

class HistoryFacade:
    def __init__(self):
        self.history_file = config.HISTORY_FILE

    def save_calculation(self, operation, numbers, result):
        """Simplified method to save calculation results."""
        data = pd.DataFrame([{
            "Operation": operation,
            "data": numbers,
            "Result": result
        }])
        file_size = os.path.getsize(self.history_file)
        if file_size == 0:
            with open(self.history_file, 'w') as f:
                f.write("Operation,Data,Result\n")

        data.to_csv(self.history_file, mode='a', header=False, index=False)

    def load_history(self):
        """Simplified method to load calculation history."""
        return pd.read_csv(self.history_file)

    def clear_history(self):
        """Simplified method to clear calculation history."""
        open(self.history_file, 'w').close()
