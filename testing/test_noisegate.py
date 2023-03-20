import pytest

# Import the noisegate function from your code here
from new_effects import noisegate


def test_noisegate():
    # Test the function with a known input and expected output
    assert noisegate(0.5, 0.2) == pytest.approx(0.0, abs=1e-2)

    # Test the function with another input
    assert noisegate(0.1, 0.2) == pytest.approx(0.0, abs=1e-3)

    # Test the function with a negative input
    assert noisegate(-0.3, 0.2) == pytest.approx(0.0, abs=1e-3)

    # Test the function with a threshold equal to zero
    assert noisegate(0.5, 0) == pytest.approx(0.0, abs=1e-2)

    # Test the function with a threshold larger than the input
    assert noisegate(0.1, 0.5) == pytest.approx(0.0, abs=1e-3)

    # Test the function with a threshold smaller than the input
    assert noisegate(0.5, 0.1) == pytest.approx(0.0, abs=1e-2)

#run it like this: python -m pytest .\testing\test_noisegate.py