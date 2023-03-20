from tkinter import N
from scipy.io import wavfile
import numpy as np
from scipy.signal import butter, lfilter
from matplotlib import pyplot

fajlnev = "gitar.wav"

fs, signal_int16 = wavfile.read(fajlnev)
signal_float64 = signal_int16.astype(float) / 2**15
atk_time = 0.05
rel_time = 0.02

time = 0
z = np.zeros(2)
atk_alpha = np.exp((-np.log(9))/(fs * atk_time))
rel_alpha = np.exp((-np.log(9))/(fs * rel_time))

def noisegate(data_in: float, threshhold: float = 0.2) -> float:
    temp = data_in
    global time
    time += 1 / fs
    if abs(temp) >= threshhold:
        Gc = 1
    else:
        Gc = 0
    if time > threshhold and Gc <= z[1]:
        z[0] = atk_alpha*z[1] + (1 - atk_alpha)*Gc
    else:
        if time <= threshhold:
            z[0] = z[1]
        else:
            if Gc > z[1]:
                z[0] = rel_alpha*z[1] + (1-rel_alpha)*Gc
                time = 0
    z[1] = z[0]
    return temp*z[0]

y = np.zeros_like(signal_float64)

for (i, x_i) in enumerate(signal_float64):
    y[i] = noisegate(x_i, 0.05) * 2**15 * 20

pyplot.plot(signal_int16)
pyplot.plot(y)
pyplot.show()

wavfile.write("noisegate.wav", fs , y.astype(np.int16))

def butterworth_eq(signal, fs, low_cutoff, high_cutoff, low_gain, mid_gain, high_gain):
    low_b, low_a = butter(4, low_cutoff / fs, 'low')
    high_b, high_a = butter(4, high_cutoff / fs, 'high')
    mid_b, mid_a = butter(4, [low_cutoff / fs, high_cutoff / fs], 'bandpass')
    
    low_signal = lfilter(low_b, low_a, signal)
    mid_signal = lfilter(mid_b, mid_a, signal)
    high_signal = lfilter(high_b, high_a, signal)
    
    filtered_signal = low_gain * low_signal + mid_gain * mid_signal + high_gain * high_signal
    
    return filtered_signal

filtered_signal = butterworth_eq(y, fs, 500, 10000, 0.6, 1.4, 0.9)
pyplot.plot(signal_int16)
pyplot.plot(filtered_signal)
pyplot.show()

wavfile.write("butter.wav", fs , filtered_signal.astype(np.int16))