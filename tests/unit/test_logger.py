import unittest
import os
from utils.logger import Logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.log_file = 'test.log'
        self.logger = Logger(log_file=self.log_file)

    def tearDown(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_logging_info(self):
        self.logger.info("This is an info message.")
        with open(self.log_file, 'r') as file:
            logs = file.read()
            self.assertIn("INFO - This is an info message.", logs)

    def test_logging_error(self):
        self.logger.error("This is an error message.")
        with open(self.log_file, 'r') as file:
            logs = file.read()
            self.assertIn("ERROR - This is an error message.", logs)

if __name__ == "__main__":
    unittest.main()
