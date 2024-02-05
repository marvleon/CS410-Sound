# Clipped Assignment

# Marvin Leon CS410

## Build Instructions

1. **Environment Setup**: Ensure Python 3 is installed on your system. You will also need `pip` for installing Python packages.

2. **Install Dependencies**: Run the following command to install the necessary Python libraries:
   ```sh
   pip install numpy scipy
   ```

## Overview

This project consists of a Python script designed to generate and save two types of sine waves as WAV files. The first file, `sine.wav`, contains a standard sine wave at 440Hz. The second file, `clipped.wav`, also generates a 440Hz sine wave but clips the amplitude to a specific range to show wave clipping effects. The script uses the `numpy` library to generate sine wave samples and the `scipy` library to write these samples to WAV files.

## How It Works

### Sine Wave Generation

- The script generates a sine wave with a frequency of 440Hz, which is the standard pitch for musical tuning.
- The sample rate is set at 48000 samples per second, providing high fidelity for the generated audio.
- The duration of the wave is 1 second.
- The amplitude of the sine wave for `sine.wav` is set to a quarter of the maximum possible value for 16-bit audio, which corresponds to the range [-8192, 8192].
- For `clipped.wav`, the script initially aims for a half-maximum amplitude but clips it to the same range as `sine.wav` to prevent distortion.

### Clipping Mechanism

- The `numpy.clip` function is used to ensure that the amplitude of the `clipped.wav` sine wave does not exceed the specified limits of -8192 and 8192.

### Conversion to 16-bit Audio

- The generated samples, initially in 32-bit float format, are scaled to fit the 16-bit signed integer format used in WAV files.
- This conversion ensures compatibility with standard audio players and maintains the fidelity of the generated sound.
