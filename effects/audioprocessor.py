from scipy.io import wavfile
import os
 
class AudioProcessor:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.fs, self.signal_int16 = wavfile.read(self.input_file_path)
        self.signal_float64 = self.signal_int16.astype(float) / 2 ** 15

    def write_output_file(self, signal, file_name):
        file_path = os.path.join(self.output_file_path, file_name)
        wavfile.write(file_path, self.fs, signal)

    def apply_effect_and_save(self, effect_func):
        effect_name = effect_func.__name__
        output_file_name = effect_name.lower() + ".wav"
        signal = effect_func(self.signal_float64) * 2 ** 15
        self.write_output_file(signal.astype('int16'), output_file_name)

