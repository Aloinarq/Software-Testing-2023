import numpy as np


class Reverb:
    def __init__(self, fs, duration_sec: float = 0.5, amplitude: float = 0.8):
        self.fs = fs
        self.duration_sec = duration_sec
        self.amplitude = amplitude

    def apply_basic_delay(self, signal):
        delay_len_samples = round(self.duration_sec * self.fs)
        zero_padding_signal = np.zeros(delay_len_samples)
        delayed_sig = np.concatenate((zero_padding_signal, signal))
        signal = np.concatenate((signal, zero_padding_signal))
        summed_sig = (signal + self.amplitude * delayed_sig).astype(np.int16)
        return summed_sig

    def apply_convolutional_delay(self, signal):
        delay_len_samples = round(self.duration_sec * self.fs)
        impulse_response = np.zeros(delay_len_samples)
        impulse_response[0] = 1
        impulse_response[-1] = self.amplitude
        output_sig = (np.convolve(signal, impulse_response) * 2 ** 15).astype(np.int16)
        return output_sig
