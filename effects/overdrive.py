import numpy as np
import os
import sys
from utils.utils import clip

# Get the path to the directory containing the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the path to the utils directory
utils_dir = os.path.join(script_dir, 'utils')

# Add the utils directory to the system path
sys.path.append(utils_dir)

class Overdrive:
    def __init__(self, amplitude: float = 1.0, gain: float = 1.0):
        self.amplitude = amplitude
        self.gain = gain

    def apply_hard_clipping(self, data_in: float) -> float:
        applied_hard_clip = self.gain * data_in
        return clip(applied_hard_clip)

    def apply_soft_clipping_1(self, data_in: float) -> float:
        applied_soft_clip = self.amplitude * np.tanh(self.gain * data_in)
        return clip(applied_soft_clip)

    def apply_soft_clipping_2(self, data_in: float) -> float:
        applied_soft_clip = self.amplitude * np.arctan(self.gain * data_in)
        return clip(applied_soft_clip)
