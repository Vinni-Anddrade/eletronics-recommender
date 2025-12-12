import logging
import os
from datetime import datetime


LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

current_time = datetime.now().strftime("%Y-%m-%d")
LOG_FILE = os.path.join(LOGS_DIR, f"{current_time}.log")

logging.basicConfig(
    filename=LOG_FILE,
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
