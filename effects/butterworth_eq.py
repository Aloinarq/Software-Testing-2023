from scipy.signal import butter, lfilter

class ButterworthEQ:
    def __init__(self, fs, low_cutoff, high_cutoff, low_gain, mid_gain, high_gain):
        self.fs = fs
        self.low_b, self.low_a = butter(4, low_cutoff / fs, 'low')
        self.high_b, self.high_a = butter(4, high_cutoff / fs, 'high')
        self.mid_b, self.mid_a = butter(4, [low_cutoff / fs, high_cutoff / fs], 'bandpass')
        self.low_gain = low_gain
        self.mid_gain = mid_gain
        self.high_gain = high_gain

    def apply(self, signal):
        low_signal = lfilter(self.low_b, self.low_a, signal)
        mid_signal = lfilter(self.mid_b, self.mid_a, signal)
        high_signal = lfilter(self.high_b, self.high_a, signal)
        filtered_signal = self.low_gain * low_signal + self.mid_gain * mid_signal + self.high_gain * high_signal
        return filtered_signal