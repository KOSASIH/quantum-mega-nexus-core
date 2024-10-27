import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from utils.data_handler import DataHandler
from utils.logger import Logger

# Initialize logger
logger = Logger()

def load_data(file_path):
    """Load climate data from a CSV file."""
    logger.info(f"Loading climate data from {file_path}")
    data = DataHandler.read_csv(file_path)
    return pd.DataFrame(data)

def preprocess_data(df):
    """Preprocess the climate data for modeling."""
    logger.info("Preprocessing climate data...")
    df.fillna(method='ffill', inplace=True)  # Forward fill missing values
    X = df[['temperature', 'humidity', 'CO2']]  # Features
    y = df['crop_yield']                         # Target variable
    return X, y

def train_model(X, y):
    """Train a Linear Regression model."""
    logger.info("Splitting data into training and testing sets...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    logger.info("Training Linear Regression model...")
    model = LinearRegression()
    model.fit(X_train, y_train)

    logger.info("Evaluating model...")
    predictions = model.predict(X_test)
    return predictions, y_test

def plot_results(predictions, actual):
    """Plot the predicted vs actual crop yields."""
    logger.info("Plotting results...")
    plt.figure(figsize=(10, 6))
    plt.scatter(actual, predictions, color='blue')
    plt.plot([actual.min(), actual.max()], [actual.min(), actual.max()], color='red', lw=2)
    plt.xlabel('Actual Crop Yield')
    plt.ylabel('Predicted Crop Yield')
    plt.title('Actual vs Predicted Crop Yield')
    plt.grid()
    plt.show()

def main():
    """Main function to run the climate modeling example."""
    data_file = 'climate_data.csv'  # Path to your dataset
    df = load_data(data_file)
    X, y = preprocess_data(df)
    predictions, actual = train_model(X, y)
    plot_results(predictions, actual)

if __name__ == "__main__":
    main()
