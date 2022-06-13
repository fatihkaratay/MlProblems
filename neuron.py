import numpy as np


class Neuron:
    # Don't change anything in the `__init__` function.
    def __init__(self, examples):
        np.random.seed(42)
        # Three weights: one for each feature and one more for the bias.
        self.weights = np.random.normal(0, 1, 3 + 1)
        self.examples = examples
        self.train()

    # Don't use regularization.
    # Use mini-batch gradient descent.
    # Use the sigmoid activation function.
    # Use the defaults for the function arguments.
    def train(self, learning_rate=0.01, batch_size=10, epochs=200):
        # Write your code here.
        pass

    # Return the probability—not the corresponding 0 or 1 label.
    def predict(self, features):
        # Write your code here.
        pass
