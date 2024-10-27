import json
import csv

class DataHandler:
    @staticmethod
    def read_json(file_path):
        """Read data from a JSON file."""
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def write_json(file_path, data):
        """Write data to a JSON file."""
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def read_csv(file_path):
        """Read data from a CSV file."""
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    @staticmethod
    def write_csv(file_path, data):
        """Write data to a CSV file."""
        with open(file_path, 'w', newline='') as file:
            if data:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)

# Example usage
if __name__ == "__main__":
    # JSON example
    json_data = {'name': 'Quantum Nexus', 'version': 1.0}
    DataHandler.write_json('data.json', json_data)
    loaded_json = DataHandler.read_json('data.json')
    print("Loaded JSON Data:", loaded_json)

    # CSV example
    csv_data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
    DataHandler.write_csv('data.csv', csv_data)
    loaded_csv = DataHandler.read_csv('data.csv')
    print("Loaded CSV Data:", loaded_csv)
