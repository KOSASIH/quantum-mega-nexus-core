import logging
import os

class Logger:
    def __init__(self, log_file='app.log', level=logging.DEBUG):
        """Initialize the logger with a specified log file and logging level."""
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)

        # Create a file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        # Create a formatter and set it for both handlers
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def debug(self, message):
        """Log a debug message."""
        self.logger.debug(message)

    def info(self, message):
        """Log an info message."""
        self.logger.info(message)

    def warning(self, message):
        """Log a warning message."""
        self.logger.warning(message)

    def error(self, message):
        """Log an error message."""
        self.logger.error(message)

    def critical(self, message):
        """Log a critical message."""
        self.logger.critical(message)

# Example usage
if __name__ == "__main__":
    logger = Logger()
    logger.info("Logger initialized.")
    logger.debug("This is a debug message.")
