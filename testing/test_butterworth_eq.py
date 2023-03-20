import numpy as np
from scipy.io import wavfile
import pytest

from new_effects import butterworth_eq


@pytest.fixture(scope="module")
def audio_signal():
    """Load an audio signal for testing."""
    fs, signal = wavfile.read("gitar.wav")
    return signal, fs


def test_butterworth_eq(audio_signal):
    signal, fs = audio_signal
    low_cutoff = 500
    high_cutoff = 10000
    low_gain = 0.6
    mid_gain = 1.4
    high_gain = 0.9

    # Apply butterworth filter
    filtered_signal = butterworth_eq(signal, fs, low_cutoff, high_cutoff, low_gain, mid_gain, high_gain)

    # Check that the length of the filtered signal is the same as the input signal
    assert len(filtered_signal) == len(signal)

    # Check that the maximum value of the filtered signal is less than or equal to 16000
    assert np.max(np.abs(filtered_signal)) <= 16000

    # Check that the filtered signal is not equal to the input signal
    assert not np.allclose(filtered_signal, signal)

#run it like this: python -m pytest .\testing\test_butterworth_eq.py 