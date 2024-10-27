import unittest
import json
import os
from utils.config import Config

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config_file = 'test_config.json'
        self.config_data = {'key1': 'value1', 'key2': 'value2'}
        with open(self.config_file, 'w') as file:
            json.dump(self.config_data, file)

    def tearDown(self):
        if os.path.exists(self.config_file):
            os.remove(self.config_file)

    def test_load_config(self):
        config = Config(config_file=self.config_file)
        self.assertEqual(config.get('key1'), 'value1')

    def test_set_config(self):
        config = Config(config_file=self.config_file)
        config.set('key3', 'value3')
        self.assertEqual(config.get('key3'), 'value3')

if __name__ == "__main__":
    unittest.main()
