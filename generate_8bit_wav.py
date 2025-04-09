import numpy as np
import wave

# Settings
filename = "sample.wav"
duration = 1.0       # seconds
frequency = 440      # Hz (A4)
sample_rate = 8000   # samples per second
amplitude = 127      # max amplitude for 8-bit (0 to 255)
offset = 128         # 8-bit WAV is unsigned

# Generate sine wave
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
samples = amplitude * np.sin(2 * np.pi * frequency * t) + offset
samples = samples.astype(np.uint8)

# Save to WAV file
with wave.open(filename, "wb") as wav_file:
    wav_file.setnchannels(1)          # Mono
    wav_file.setsampwidth(1)          # 8-bit
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(samples.tobytes())

print(f"✅ Generated {filename} - {frequency}Hz tone, {duration}s, 8-bit mono")
