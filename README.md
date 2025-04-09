# Huffman Compression of WAV Audio using ESP32

## Project Overview

This project demonstrates the application of Huffman coding for compressing raw audio data from an 8-bit PCM WAV file using an ESP32 microcontroller. A 256-byte audio sample is sent to the ESP32 via serial communication. The ESP32 performs Huffman encoding on the data and returns the encoded bitstream and compression statistics. Python scripts are used for generating the WAV file, sending the data, and visualizing the results.

---

## Objective

To implement Huffman compression of audio data on a resource-constrained microcontroller and evaluate compression efficiency through visualization and manual verification.

---

## Components and Tools

### Hardware
- ESP32 Development Board
- USB Cable
- Computer (with Python and Arduino IDE)

### Software & Libraries
- Arduino IDE
- Python 3
- Python Libraries:
  - `wave`
  - `numpy`
  - `matplotlib`
  - `pyserial`

---

## Project Workflow

1. Generate a synthetic 8-bit PCM WAV file using Python.
2. Send 256 bytes of audio sample data from the WAV file to the ESP32 via serial.
3. ESP32 reads the bytes, constructs a Huffman tree, generates a codebook, and compresses the data.
4. Compressed data and statistics (original vs compressed size) are printed over serial.
5. Python script is used to visualize waveform, amplitude histogram, and compression ratio.

---

## Conclusion

This project validates the use of Huffman coding for real-time audio data compression on a microcontroller. The implementation confirms the algorithm's effectiveness for compressing WAV audio samples and showcases how embedded systems can be integrated with data visualization tools on a PC.
