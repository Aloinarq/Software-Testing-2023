import numpy as np

class Noisegate:
    def __init__(self, fs, atk_time=0.05, rel_time=0.02):
        self.fs = fs
        self.atk_alpha = np.exp((-np.log(9))/(fs * atk_time))
        self.rel_alpha = np.exp((-np.log(9))/(fs * rel_time))
        self.time = 0
        self.z = np.zeros(2)

    def apply(self, data_in, threshold=0.2):
        temp = data_in
        self.time += 1 / self.fs
        if abs(temp) >= threshold:
            Gc = 1
        else:
            Gc = 0
        if self.time > threshold and Gc <= self.z[1]:
            self.z[0] = self.atk_alpha * self.z[1] + (1 - self.atk_alpha) * Gc
        else:
            if self.time <= threshold:
                self.z[0] = self.z[1]
            else:
                if Gc > self.z[1]:
                    self.z[0] = self.rel_alpha * self.z[1] + (1 - self.rel_alpha) * Gc
                    self.time = 0
        self.z[1] = self.z[0]
        return temp * self.z[0]