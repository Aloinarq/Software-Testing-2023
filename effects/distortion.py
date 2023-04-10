import numpy as np
from ..utils.utils import clip


class Distortion:
    def __init__(self, gain: float = 1.0):
        self.gain = gain

    def apply(self, data_in: float) -> float:
        applied_distortion = np.sign(data_in) * (1.0 - np.exp(self.gain * np.sign(data_in) * data_in))
        return clip(applied_distortion)
