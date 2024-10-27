import time
import random
from data_handler import DataHandler

def test_performance():
    data = [{'name': f'User {i}', 'age': random.randint(18, 65)} for i in range(10000)]
    start_time = time.time()
    DataHandler.write_csv('performance_test.csv', data)
    end_time = time.time()
    print(f"Writing 10,000 records to CSV took {end_time - start_time:.2f} seconds")

    start_time = time.time()
    data = DataHandler.read_csv('performance_test.csv')
    end_time = time.time()
    print(f"Reading 10,000 records from CSV took {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    test_performance()
