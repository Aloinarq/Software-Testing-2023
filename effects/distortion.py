import numpy as np


class Distortion:
    def __init__(self, gain: float = 1.0):
        self.gain = gain

    def apply(self, data_in: float) -> float:
        temp = np.sign(data_in) * (1.0 - np.exp(self.gain * np.sign(data_in) * data_in))
        return self.clip(temp)

    def clip(self, value: float) -> float:
        return np.clip(value, -1.0, 1.0)
