import numpy as np


class Delay:
    def __init__(self, fs, duration_sec: float = 0.5, amplitude: float = 0.8):
        self.fs = fs
        self.duration_sec = duration_sec
        self.amplitude = amplitude

    def apply_convolutional_delay(self, signal):
        delay_len_samples = round(self.duration_sec * self.fs)
        impulse_response = np.zeros(delay_len_samples)
        impulse_response[0] = 1
        impulse_response[-1] = self.amplitude
        output_sig = (np.convolve(signal, impulse_response) * 2 ** 15).astype(np.int16)
        return output_sig
