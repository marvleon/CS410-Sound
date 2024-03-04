import numpy as np
from scipy.io import wavfile
from scipy.signal import iirfilter, sosfilt

# Applies high-pass filter to the input samples, returns the filtered samples
def high_pass_filter(samples, fs, cutoff=4000):
    # Fourth order filter
    sos = iirfilter(N=4, Wn=cutoff/(fs/2), btype='high', ftype='butter', output='sos')
    # Filter the samples
    filtered_samples = sosfilt(sos,samples)
    return filtered_samples

# Detects the peak in the input samples, returns the value
def peak_detector(samples):
    peak_value = np.max(np.abs(samples))
    return peak_value

# Normalizes input samples
def normalize_effect(samples, q):
    p = peak_detector(samples) # Detect peak in input samples
    normalized_samples = samples * (q / p) # Scale samples 
    return normalized_samples

# Applies clipping distortion to the input samples
def clipping_distortion(samples):
    normalized_samples = normalize_effect(samples, 1.0)
    clipped_samples = np.clip(normalized_samples, -0.4, 0.4)
    return clipped_samples

# Mixes two sets of input samples
def wet_dry_mixer(s1, s2):
    return ((0.8 * s1) + (0.2 * s2))

# Processes samples from input file to create echomorphed output file
def process_echo(input_file, output_file):
    fs, samples = wavfile.read(input_file)
    output = [samples.astype(np.float32)] # Convert to float

    # Loop to generate the echo
    for _ in range(9):  
        p = peak_detector(output[-1]) # Detect peak of the last processed sample
        d = clipping_distortion(output[-1]) #Apply clipping
        h = high_pass_filter(d, fs) # Apply HPF
        n = normalize_effect(h, p) # Normalize
        m = wet_dry_mixer(n, output[-1]) # Mix with processed samples
        new_sample = m * 0.7 # Scale down
        output.append(new_sample) # Add new samples to the output list

    # Concatenate all samples in the output list to form the final output
    final_output = np.concatenate(output, axis=0)
    final_peak = peak_detector(final_output) # Get peak
    final_output_normalized = final_output * (0.5 / final_peak) # Normalize

    wavfile.write(output_file, fs, final_output_normalized)

process_echo('voice-note.wav', 'output.wav')