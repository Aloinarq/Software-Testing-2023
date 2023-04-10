import numpy as np

def clip(value: float) -> float:
    return np.clip(value, -1.0, 1.0)