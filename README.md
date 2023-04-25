# Introduction

This repository is dedicated to the development of a simulation of a digital guitar pedal using Python and the Pytest testing framework. The aim of this project is to create a high-quality audio effect for guitarists, which can be easily integrated into their recording sessions. This is a project I've been working on for a while now, the actual realtime effects will only be available on an STM32 NUCLEO-G491RE microcontroller and its effects will be written in C++ but the testing of the effects' behaviour can be tested in python anyway, with the exception of being able to use them in a live session, this way it's only postprocessing.

## Pytest

Pytest is a popular testing framework for Python, which provides an easy-to-use and efficient way of writing and executing tests. It offers a range of features, such as automatic discovery of test modules and functions, rich reporting capabilities, and the ability to run tests in parallel. Pytest can be used for all types of testing, including unit, integration, and functional testing.

In this project, Pytest will be used to test the functionality and performance of the simulated guitar pedal's audio effects. The tests will cover a range of scenarios, including different input signals, parameter settings, and output formats. Pytest will help to ensure that the audio effects are working correctly, and that any changes to the code do not introduce any regressions.

## Digital Guitar Pedal

The simulated digital guitar pedal will be developed using Python, with a focus on digital signal processing techniques. The pedal will aim to provide a range of high-quality audio effects, such as distortion, oerdrive, delay and also an EQ. The effects will be designed to be adjustable, with parameters such as gain, time, and feedback, to allow guitarists to customize their sound.

The development of the guitar pedal will involve a range of techniques, including filtering, convolution, and modulation. The Python libraries Numpy, Scipy, and Pytest will be used to implement these techniques, as well as to visualize the results of the tests.

# Conclusion

In summary, this repository will aim to create a digital guitar pedal using Python, with a focus on digital signal processing techniques. Pytest will be used to test the functionality and performance of the audio effects. The final product will provide guitarists with a range of high-quality audio effects, which can be easily integrated into their recordings.
