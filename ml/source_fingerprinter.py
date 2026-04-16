import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump, load

class SourceFingerprinter:
    def __init__(self):
        self.model = None

    def train(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Train the model using the provided features and labels.

        :param X: Features matrix (shape: n_samples x n_features)
        :param y: Labels vector (shape: n_samples,)
        """
        # Split the data into training and validation sets
        X_train, X_val, y_train, y_val = train_test_split(X, y, 
test_size=0.2, random_state=42)

        # Initialize and train the RandomForestClassifier
        self.model = RandomForestClassifier(n_estimators=100, 
random_state=42)
        self.model.fit(X_train, y_train)

    def predict(self, features: list) -> str:
        """
        Predict the source category for a given set of features.

        :param features: List of feature values (length: n_features)
        :return: Predicted source category as a string
        """
        # Convert the list to a numpy array
        features_array = np.array([features])
        
        # Ensure the input has the correct shape
        if features_array.shape[1] != 7:
            raise ValueError("Input features must have exactly 7
elements")

        # Predict using the trained model
        prediction = self.model.predict(features_array)
        return prediction[0]

    def save(self, file_path: str) -> None:
        """
        Save the trained model to a file.

        :param file_path: Path where the model will be saved
        """
        dump(self.model, file_path)

    def load(self, file_path: str) -> None:
        """
        Load the trained model from a file.

        :param file_path: Path to the model file
        """
        self.model = load(file_path)

    def feature_importance(self) -> np.ndarray:
        """
        Calculate and return the feature importances of the trained
model.

        :return: Array of feature importances (length: n_features)
        """
        if self.model is None:
            raise ValueError("Model not trained yet")
        
        return self.model.feature_importances_

# Example usage:
if __name__ == "__main__":
    # Simulate features and labels (replace with actual data)
    X = np.random.rand(100, 7)  # Replace with actual data
    y = np.random.randint(4, size=100)  # Labels: "vehicular", 
"industrial", "construction", "background"

    try:
        fingerprinter = SourceFingerprinter()
        fingerprinter.train(X, y)

        # Predict a sample
        features_sample = [X[0]]  # Replace with actual feature values      
for prediction
        predicted_category = fingerprinter.predict(features_sample)
        print("Predicted category:", predicted_category)

        # Save the model
        fingerprinter.save('ml/models/fingerprinter.pkl')

        # Load the model
        fingerprinter.load('ml/models/fingerprinter.pkl')

        # Predict again after loading
        loaded_predicted_category = 
fingerprinter.predict(features_sample)
        print("Loaded model predicted category:", 
loaded_predicted_category)

        # Get feature importances
        importances = fingerprinter.feature_importance()
        print("Feature importances:", importances)
    except ValueError as e:
        print(e)