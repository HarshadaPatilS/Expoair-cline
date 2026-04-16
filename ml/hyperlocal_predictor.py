import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

class HyperLocalPredictor:
    def __init__(self):
        self.model = None

    def build_model(self):
        """
        Build and compile the LSTM model.
        """
        model = Sequential()
        
        # Add an LSTM layer with 64 units
        model.add(LSTM(64, input_shape=(24, 5), 
return_sequences=True))
        
        # Add another LSTM layer with 64 units
        model.add(LSTM(64))
        
        # Add a Dense layer for the output with shape (3,)
        model.add(Dense(3))
        
        # Compile the model
        model.compile(optimizer='adam', loss='mse')
        
        self.model = model

    def predict(self, sequence: np.ndarray) -> list[float]:
        """
        Make predictions on input sequences.

        :param sequence: Input sequence of shape (24, 5)
        :return: List of predicted values for the next 3 hours
        """
        # Ensure the input is in the correct format
        if sequence.shape != (24, 5):
            raise ValueError("Input sequence must have shape (24, 5)")
        
        # Make predictions
        prediction = self.model.predict(sequence)
        
        # Return the first three predicted values as a list
        return prediction[0][:3].tolist()

    def save_model(self, file_path: str) -> None:
        """
        Save the model to a file.

        :param file_path: Path where the model will be saved
        """
        self.model.save(file_path)

    def load_model(self, file_path: str) -> None:
        """
        Load the model from a file.

        :param file_path: Path to the model file
        """
        self.model = self.model.load_weights(file_path)

# Example usage:
if __name__ == "__main__":
    predictor = HyperLocalPredictor()
    predictor.build_model()

    # Simulate input sequence (replace with actual data)
    input_sequence = np.random.rand(24, 5)  # Replace with actual data

    try:
        predicted_values = predictor.predict(input_sequence)
        print("Predicted values:", predicted_values)

        # Save the model
        predictor.save_model('ml/models/hyperlocal_lstm.h5')

        # Load the model
        predictor.load_model('ml/models/hyperlocal_lstm.h5')

        # Predict again after loading
        loaded_predicted_values = predictor.predict(input_sequence)
        print("Loaded model predicted values:", 
loaded_predicted_values)
    except ValueError as e:
        print(e)