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

    def apply_effect_and_save(self, effect_func, file_name):
        signal = effect_func(self.signal_float64) * 2 ** 15
        self.write_output_file(signal.astype('int16'), file_name)

if __name__ == "__main__":
    input_file_path = os.path.abspath("./audio_inputs/gitar.wav")
    output_file_path = os.path.abspath("./audio_outputs/")

    processor = AudioProcessor(input_file_path, output_file_path)

    # Example usage: apply an overdrive effect with soft clipping 1 and save the output to file
    from overdrive import Overdrive
    from distortion import Distortion
    from reverb import Reverb
    overdrive = Overdrive(amplitude=0.9, gain=5.0)
    distortion = Distortion(gain=5.0)
    reverb = Reverb(processor.fs, duration_sec=0.5, amplitude=0.8)
    processor.apply_effect_and_save(overdrive.apply_soft_clipping_1, "overdrive_soft_clipping_1.wav")
    processor.apply_effect_and_save(reverb.apply_basic_delay, "basic_delay.wav")
    processor.apply_effect_and_save(distortion.apply, "distortion.wav")
