import pytest
import numpy as np
from effects.distortion import Distortion
from effects.overdrive import Overdrive
from effects.delay import Delay
from effects.butterworth_eq import ButterworthEQ

class Tests:
    def test_distortion(self):
        # Test case 1
        distortion = Distortion(gain=2.0)
        data_in = 0.5
        distorted_data = distortion.apply(data_in)
        assert distorted_data == pytest.approx(-1.0)

        # Test case 2
        distortion = Distortion(gain=1.0)
        data_in = 0.5
        distorted_data = distortion.apply(data_in)
        assert distorted_data == pytest.approx(-0.64, abs=0.01)

    def test_overdrive(self):
        overdrive = Overdrive(amplitude=2.0, gain=3.0)
        data_in = 0.5
        assert overdrive.apply_hard_clipping(data_in) == pytest.approx(1.0)
        assert overdrive.apply_soft_clipping_1(data_in) == pytest.approx(1.098, abs=0.1)
        assert overdrive.apply_soft_clipping_2(data_in) == pytest.approx(1.057, abs=0.1)

    def test_convolutional_delay(self):
        fs = 8000
        duration_sec = 0.5
        amplitude = 0.8
        delay = Delay(fs, duration_sec, amplitude)
        signal = np.array([1, 2, 3])
        impulse_response = np.zeros(round(duration_sec * fs))
        impulse_response[0] = 1
        impulse_response[-1] = amplitude
        expected_output = (np.convolve(signal, impulse_response) * 2 ** 15).astype(np.int16)
        output = delay.apply_convolutional_delay(signal)
        assert np.allclose(output, expected_output)

    def test_butterworthEQ(self):
        fs = 8000
        low_cutoff = 500
        high_cutoff = 2000
        low_gain = 0.8
        mid_gain = 1.2
        high_gain = 1.5
        eq = ButterworthEQ(fs, low_cutoff, high_cutoff, low_gain, mid_gain, high_gain)
        signal = np.random.randn(fs)
        output = eq.apply(signal)
        
        # Verify that the output has the same shape as the input signal
        assert output.shape == signal.shape

#run it like this: python -m pytest testing\tests.py