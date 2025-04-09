import wave
import serial
import time
import numpy as np

# --------- Serial Config ----------
PORT = "COM19"  # Change to your ESP32 port
BAUD = 115200
ser = serial.Serial(PORT, BAUD)
time.sleep(2)

# --------- Load WAV File ----------
wav = wave.open("sample.wav", "rb")
n_channels, sampwidth, framerate, n_frames, _, _ = wav.getparams()

if sampwidth != 1:
    raise ValueError("Only 8-bit PCM WAV supported for this demo!")

frames = wav.readframes(256)  # Get 256 samples
wav.close()

print(f"Sending {len(frames)} bytes to ESP32...")
ser.write(frames)  # Send raw audio bytes

# --------- Listen to ESP32 output ----------
while True:
    try:
        line = ser.readline().decode().strip()
        if line:
            print("ESP32:", line)
    except:
        break
