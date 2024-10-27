import unittest
import os
from utils.data_handler import DataHandler

class TestDataHandler(unittest.TestCase):
    def setUp(self):
        self.json_file = 'test_data.json'
        self.csv_file = 'test_data.csv'
        self.test_data_json = {'name': 'Quantum Nexus', 'version': 1.0}
        self.test_data_csv = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        DataHandler.write_json(self.json_file, self.test_data_json)
        DataHandler.write_csv(self.csv_file, self.test_data_csv)

    def tearDown(self):
        if os.path.exists(self.json_file):
            os.remove(self.json_file)
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)

    def test_read_json(self):
        data = DataHandler.read_json(self.json_file)
        self.assertEqual(data, self.test_data_json)

    def test_read_csv(self):
        data = DataHandler.read_csv(self.csv_file)
        self.assertEqual(data, self.test_data_csv)

if __name__ == "__main__":
    unittest.main()
