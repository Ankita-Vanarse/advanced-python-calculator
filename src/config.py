import os
from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
HISTORY_FILE = os.getenv("HISTORY_FILE", "./data/history.csv")
LOG_FILE = os.getenv("LOG_FILE", "./logs/log.log")
