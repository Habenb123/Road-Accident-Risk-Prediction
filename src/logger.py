import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


# Create log file with today's date
LOG_FILE = os.path.join(
    LOG_DIR,
    f"{datetime.now().strftime('%Y-%m-%d')}.log"
)


# Create logger
logger = logging.getLogger("road_risk")
logger.setLevel(logging.INFO)


# Prevent duplicate handlers if the module is imported multiple times
if not logger.handlers:

    # Log format
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s - %(name)s - %(message)s"
    )

    # File handler
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
