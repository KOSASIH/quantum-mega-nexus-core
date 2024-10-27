import numpy as np
from sklearn.linear_model import LinearRegression

class AISolver:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        """Train the AI model on the provided data."""
        self.model.fit(X, y)

    def predict(self, X):
        """Make predictions using the trained model."""
        return self.model.predict(X)

    def evaluate(self, X, y):
        """Evaluate the model's performance."""
        predictions = self.predict(X)
        mse = np.mean((predictions - y) ** 2)
        return mse

# Example usage
if __name__ == "__main__":
    # Sample data
    X = np.array([[1], [2], [3], [4]])
    y = np.array([2, 3, 4, 5])

    solver = AISolver()
    solver.train(X, y)
    predictions = solver.predict(np.array([[5], [6]]))
    print("Predictions:", predictions)
    print("Model Evaluation (MSE):", solver.evaluate(X, y))
