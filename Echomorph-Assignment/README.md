# Echomorph Assignment

# Marvin leon CS410 Sound

This program aims to replicate the "echomorph" effect. To achieve this, the program includes high-pass filtering (order 4 IIR), clipping distortion, normalization, and a wet/dry mix. The program reads an input WAV file, applies these effects iteratively, and writes the processed audio to a new WAV file.

Essentially:

- The input samples get stored in the list. Their peak value is found.
- The samples get distorted to get a new set of effect-samples. These are filtered through the HPF and normalized with the peak value found earlier.
- Then the input samples are mixed with the effect samples using the wet-dry mixer.
- The resulting samples are then scaled down, added to the list, and used as the next input.

I think this went well because it produces an echomorph effect. However, there is some work to be done. I think the highpass filter should be changed and made better. I used scipy to build a filter but used generic arguments. Additionally, I think standardizing the samples could make things more efficient. In the future I would like to add a prompt to allow the user to hear the sample directly and to also prompt to choose their own input files.

## Dependencies

1. **Environment Setup**: Ensure Python 3 is installed on your system. You will also need `pip` for installing Python packages.

2. **Install Dependencies**: Run the following command to install the necessary Python libraries:
   ```sh
   pip install numpy scipy
   ```

## HOW TO RUN

1. Run with an input wav file: `python echomorph.py voice-note.wav`
