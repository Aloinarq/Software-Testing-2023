import numpy as np


class Overdrive:
    def __init__(self, amplitude: float = 1.0, gain: float = 1.0):
        self.amplitude = amplitude
        self.gain = gain

    def apply_hard_clipping(self, data_in: float) -> float:
        temp = self.gain * data_in
        return self.clip(temp)

    def apply_soft_clipping_1(self, data_in: float) -> float:
        temp = self.amplitude * np.tanh(self.gain * data_in)
        return self.clip(temp)

    def apply_soft_clipping_2(self, data_in: float) -> float:
        temp = self.amplitude * np.arctan(self.gain * data_in)
        return self.clip(temp)

    def clip(self, value: float) -> float:
        return np.clip(value, -1.0, 1.0)
