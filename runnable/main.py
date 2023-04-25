import os

from effects.audioprocessor import AudioProcessor
from effects.overdrive import Overdrive
from effects.distortion import Distortion
from effects.delay import Delay
from effects.butterworth_eq import ButterworthEQ

from testing.tests import Tests

if __name__ == "__main__":    
    tests = Tests()
    tests.test_distortion()
    tests.test_overdrive
    tests.test_convolutional_delay()
    tests.test_butterworthEQ()

    input_file_path = os.path.abspath("./audio_inputs/gitar.wav")
    output_file_path = os.path.abspath("./audio_outputs/")

    processor = AudioProcessor(input_file_path, output_file_path)
    
    overdrive = Overdrive(amplitude=0.9, gain=5.0)
    distortion = Distortion(gain=5.0)
    delay = Delay(processor.fs, duration_sec=0.5, amplitude=0.8)
    butterworth_eq = ButterworthEQ(processor.fs, 500, 10000, 0.6, 1.4, 0.9)

    processor.apply_effect_and_save(distortion.apply)
    processor.apply_effect_and_save(overdrive.apply_soft_clipping_1)
    processor.apply_effect_and_save(delay.apply_convolutional_delay)
    processor.apply_effect_and_save(butterworth_eq.apply)

#run it like this: python -m runnable.main