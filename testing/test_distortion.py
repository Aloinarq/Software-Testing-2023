import numpy as np
from scipy.io import wavfile
from scipy.signal import correlate
from pytest import approx

# Import your effect functions here:
from effects import distortion

def test_distortion():
    # Test data
    data_in = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
    gain = 1.0

    # Expected output
    expected_output = np.array([-0.632121, -0.301127, 0.0, 0.301127, 0.632121])

    # Test the function
    output = distortion(data_in, gain)

    # Check if the output matches the expected output with a certain tolerance
    assert np.allclose(output, expected_output, rtol=1e-5)

#run it like this: python -m pytest .\testing\test_distortion.py