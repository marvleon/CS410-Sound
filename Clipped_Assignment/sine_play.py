import sounddevice as sd
import scipy.io.wavfile

# Load the clipped sine wave
fs, data = scipy.io.wavfile.read('clipped.wav')

# Play audio
sd.play(data, fs)
sd.wait()  # Wait until file is done playing
