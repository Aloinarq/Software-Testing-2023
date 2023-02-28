import numpy as np
from scipy.io import wavfile
from scipy.signal import correlate
from pytest import approx

def test_delay_functions():
    # Test data
    fajlnev = "gitar.wav"
    echo_duration_sec = 0.2
    delay_amplitude = 0.7

    fs, signal_int16 = wavfile.read(fajlnev)
    signal_float64 = signal_int16.astype(float) / 2**15

    delay_len_samples = round(echo_duration_sec * fs)
    zero_padding_signal = np.zeros(delay_len_samples)
    delayed_sig = np.concatenate((zero_padding_signal, signal_float64))

#Run it like this: python -m pytest .\test_delay.py