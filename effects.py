from scipy.io import wavfile
import numpy as np
import scipy.io
import matplotlib.pyplot as plt

def overdrive_hard_clipping(data_in: float, amplitude: float = 1.0, gain: float = 1.0) -> float:
    temp = gain*data_in
    if temp > 1.0:
        return 1.0
    if temp < -1.0:
        return -1.0
    return temp

def overdrive_soft_clipping_1(data_in: float, amplitude: float = 1.0, gain: float = 1.0) -> float:
    temp = amplitude * np.tanh(gain * data_in)
    if temp > 1.0:
        return 1.0
    if temp < -1.0:
        return -1.0
    return temp

def overdrive_soft_clipping_2(data_in: float, amplitude: float = 1.0, gain: float = 1.0) -> float:
    temp = amplitude * np.arctan(gain * data_in)
    if temp > 1.0:
        return 1.0
    if temp < -1.0:
        return -1.0
    return temp

def distortion(data_in: float, gain: float = 1.0) -> float:
    temp = np.sign(data_in) * (1.0 - np.exp(gain*np.sign(data_in)*data_in))
    temp = np.clip(temp, -1.0, 1.0)  # clip the values to the range [-1.0, 1.0]
    if temp > 1.0:
        return 1.0
    elif temp < -1.0:
        return -1.0
    else:
        return temp


fajlnev = "gitar.wav"
echo_duration_sec = 0.2
delay_amplitude = 0.7

fs, signal_int16 = wavfile.read(fajlnev)
signal_float64 = signal_int16.astype(float) / 2**15

y = np.zeros_like(signal_float64)
for (i, x_i) in enumerate(signal_float64):
    y[i] = overdrive_hard_clipping(x_i, 0.9, 5) * 2**15
wavfile.write("overdrive_hard_clipping.wav", fs , y.astype(np.int16))

y = np.zeros_like(signal_float64)
for (i, x_i) in enumerate(signal_float64):
    y[i] = overdrive_soft_clipping_1(x_i, 0.9, 5) * 2**15
wavfile.write("overdrive_soft_clipping_1.wav", fs , y.astype(np.int16))

y = np.zeros_like(signal_float64)
for (i, x_i) in enumerate(signal_float64):
    y[i] = overdrive_soft_clipping_2(x_i, 0.9, 5) * 2**15
wavfile.write("overdrive_soft_clipping_2.wav", fs , y.astype(np.int16))

y = np.zeros_like(signal_float64)
for (i, x_i) in enumerate(signal_float64):
    y[i] = distortion(x_i, 5) * 2**15
wavfile.write("distortion.wav", fs , y.astype(np.int16))

delay_len_samples = round(echo_duration_sec * fs)
zero_padding_signal = np.zeros(delay_len_samples)
delayed_sig = np.concatenate((zero_padding_signal, signal_float64))
signal_float64 = np.concatenate((signal_float64, zero_padding_signal))

summed_sig = (signal_float64 + delay_amplitude * delayed_sig * 2**15).astype(np.int16)
wavfile.write("basic_delay.wav", fs , summed_sig)

impulse_response = np.zeros(delay_len_samples)
impulse_response[0] = 1
impulse_response[-1] = delay_amplitude
output_sig = (np.convolve(signal_float64, impulse_response)*2**15).astype(np.int16)
wavfile.write("convolutional_delay.wav", fs , output_sig)