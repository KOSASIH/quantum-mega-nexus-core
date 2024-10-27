import json
import os

class Config:
    def __init__(self, config_file='config.json'):
        """Load configuration from a JSON file."""
        self.config_file = config_file
        self.config_data = self.load_config()

    def load_config(self):
        """Load configuration data from the JSON file."""
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file '{self.config_file}' not found.")
        
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        """Get a configuration value by key."""
        return self.config_data.get(key, default)

    def set(self, key, value):
        """Set a configuration value by key."""
        self.config_data[key] = value
        self.save_config()

    def save_config(self):
        """Save the current configuration data back to the JSON file."""
        with open(self.config_file, 'w') as file:
            json.dump(self.config_data, file, indent=4)

# Example usage
if __name__ == "__main__":
    config = Config()
    print("Current Configuration:", config.config_data)
    config.set('new_key', 'new_value')
    print("Updated Configuration:", config.get('new_key'))
