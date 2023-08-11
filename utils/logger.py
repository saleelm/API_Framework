# utils/logger.py

import logging
import os
from datetime import datetime


class Logger:
    LOG_DIRECTORY = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs")

    def __init__(self, filepath, level=logging.DEBUG):
        # Ensure the logs directory exists
        if not os.path.exists(self.LOG_DIRECTORY):
            os.makedirs(self.LOG_DIRECTORY)

        self.logger = self.setup_logger(filepath, level)

    @classmethod
    def get_log_path(cls, filepath):
        """Generate the log file path based on the test category and timestamp."""

        # Extract the test category (folder name) from the provided filepath
        test_category = os.path.basename(os.path.dirname(filepath))

        # Generate a timestamp for the filename
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

        filename = f"{test_category}_test_{timestamp}.log"
        return os.path.join(cls.LOG_DIRECTORY, filename)

    def setup_logger(self, filepath, level):
        """Setup logger for the provided test category and timestamp."""

        log_file = self.get_log_path(filepath)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        handler = logging.FileHandler(log_file)
        handler.setFormatter(formatter)

        logger_name = os.path.splitext(os.path.basename(log_file))[
            0]  # Use log filename without extension as logger name
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger
