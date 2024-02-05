import numpy as np  # Import NumPy for numerical operations
from scipy.io.wavfile import write  # Import write function from scipy to save arrays as WAV files

# Specifications
sample_rate = 48000  # Set the sample rate to 48000 samples per second, which defines how many samples are used to represent one second of audio
frequency = 440  # Set the frequency of the sound wave to 440 Hz, which is the pitch of the sound (A note)
duration = 1  # Set the duration of the sound to 1 second
max_amplitude_16_bit = 32767  # Maximum amplitude for 16-bit audio, where 32767 is the max positive value for a 16-bit signed integer
quarter_amplitude = max_amplitude_16_bit // 4  # Calculate ¼ of the maximum amplitude for a softer sound
half_amplitude = max_amplitude_16_bit // 2  # Calculate ½ of the maximum amplitude for a louder sound than the quarter but with potential clipping

# Generate time value array
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)  # Create an array of time values from 0 to 1 second, evenly spaced according to the sample rate

# Part 1: Generate sine wave (¼ amplitude)
sine_wave = quarter_amplitude * np.sin(2 * np.pi * frequency * t)  # Generate sine wave values at ¼ maximum amplitude based on the frequency and time values
sine_wave_int16 = np.int16(sine_wave)  # Convert sine wave values to 16-bit integers for WAV file compatibility
write('sine.wav', sample_rate, sine_wave_int16)  # Write the sine wave data as a 16-bit WAV file named 'sine.wav'

# Part 2: Generate clipped sine wave (½ amplitude with clipping)
clipped_sine_wave = half_amplitude * np.sin(2 * np.pi * frequency * t)  # Generate sine wave values at ½ maximum amplitude which will be clipped
# Apply clipping
clipped_sine_wave = np.clip(clipped_sine_wave, -quarter_amplitude, quarter_amplitude)  # Clip the sine wave to keep it within ±¼ maximum amplitude, producing a distorted effect
clipped_sine_wave_int16 = np.int16(clipped_sine_wave)  # Convert clipped sine wave values to 16-bit integers for WAV file compatibility
write('clipped.wav', sample_rate, clipped_sine_wave_int16)  # Write the clipped sine wave data as a 16-bit WAV file named 'clipped.wav'
