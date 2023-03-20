from scipy.io import wavfile
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
import os


class Distortion:
    def __init__(self, gain: float = 1.0):
        self.gain = gain

    def apply(self, data_in: float) -> float:
        temp = np.sign(data_in) * (1.0 - np.exp(self.gain * np.sign(data_in) * data_in))
        return self.clip(temp)

    def clip(self, value: float) -> float:
        return np.clip(value, -1.0, 1.0)


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


if __name__ == "__main__":
    file_input = os.path.abspath("./audio_inputs/gitar.wav")
    file_output = os.path.abspath("./audio_outputs/")
    fs, signal_int16 = wavfile.read(file_input)
    signal_float64 = signal_int16.astype(float) / 2 ** 15

    overdrive = Overdrive(amplitude=0.9, gain=5.0)
    distortion = Distortion(gain=5.0)
    reverb = Reverb(fs=fs, duration_sec=0.5, amplitude=0.8)

    y_overdrive_hard_clipping = np.array([overdrive.apply_hard_clipping(x) for x in signal_float64]) * 2 ** 15
    y_overdrive_soft_clipping_1 = np.array([overdrive.apply_soft_clipping_1(x) for x in signal_float64]) * 2 ** 15
    y_overdrive_soft_clipping_2 = np.array([overdrive.apply_soft_clipping_2(x) for x in signal_float64]) * 2 ** 15
    y_distortion = np.array([distortion.apply(x) for x in signal_float64]) * 2 ** 15
    y_reverb_basic_delay = reverb.apply_basic_delay(signal_int16)
    y_reverb_convolutional_delay = reverb.apply_convolutional_delay(signal_int16)

    wavfile.write(os.path.join(file_output, "overdrive_hard_clipping.wav"), fs, y_overdrive_hard_clipping)
    wavfile.write(os.path.join(file_output, "overdrive_soft_clipping_1.wav"), fs, y_overdrive_soft_clipping_1)
    wavfile.write(os.path.join(file_output, "overdrive_soft_clipping_2.wav"), fs, y_overdrive_soft_clipping_2)
    wavfile.write(os.path.join(file_output, "distortion.wav"), fs, y_distortion)
    wavfile.write(os.path.join(file_output, "basic_delay.wav"), fs, y_reverb_basic_delay)
    wavfile.write(os.path.join(file_output, "convolutional_delay.wav"), fs, y_reverb_convolutional_delay)