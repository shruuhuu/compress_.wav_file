# Huffman Compression of WAV Audio using ESP32

## Project Overview

This project demonstrates how Huffman coding can be applied to compress audio data from an 8-bit PCM WAV file using an ESP32 microcontroller. A 256-byte audio segment is transmitted from a computer to the ESP32 via serial communication. The ESP32 performs Huffman encoding, generates a binary codebook, compresses the input, and returns the encoded bitstream and statistics over serial. Python scripts are used to generate test audio, send data, and visualize results.

## Objective

To implement Huffman compression on a microcontroller, specifically ESP32, and evaluate the compression efficiency for raw audio data using Python-based tools.

## Components and Tools

### Hardware
- ESP32 Development Board
- USB Interface Cable
- Computer with Python and Arduino IDE

### Software and Libraries
- Arduino IDE
- Python 3.x
- Python Libraries:
  - `wave`
  - `numpy`
  - `matplotlib`
  - `pyserial`

## Project Workflow

1. A Python script generates or loads an 8-bit PCM WAV audio file.
2. 256 bytes of audio samples are read and sent to the ESP32 over serial.
3. The ESP32 reads the samples, calculates frequency of each byte, builds a Huffman tree, and encodes the data.
4. The ESP32 prints the generated codebook and compression statistics.
5. A separate Python script visualizes the audio waveform, amplitude histogram, and original vs. compressed bit sizes.
