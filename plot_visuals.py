import wave
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import heapq

# ---------- 1. Load WAV file ----------
wav_file = wave.open("sample.wav", "rb")
n_channels, sampwidth, framerate, n_frames, _, _ = wav_file.getparams()

if sampwidth != 1:
    raise ValueError("Only 8-bit PCM WAV supported")

frames = wav_file.readframes(256)  # Read 256 samples
samples = np.frombuffer(frames, dtype=np.uint8)
wav_file.close()

print("✅ Loaded 256 samples from WAV file")

# ---------- 2. Huffman Encoding ----------
class Node:
    def __init__(self, val=None, freq=0):
        self.val = val
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other): return self.freq < other.freq

def build_tree(data):
    freq = Counter(data)
    heap = [Node(val, freq[val]) for val in freq]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]

def make_codes(node, prefix="", codebook={}):
    if node:
        if node.val is not None:
            codebook[node.val] = prefix
        make_codes(node.left, prefix + "0", codebook)
        make_codes(node.right, prefix + "1", codebook)

def huffman_encode(data):
    root = build_tree(data)
    codebook = {}
    make_codes(root, "", codebook)
    encoded = ''.join(codebook[s] for s in data)
    return encoded, codebook

encoded_bits, codebook = huffman_encode(samples)

# ---------- 3. Visualize ----------
plt.figure(figsize=(12, 6))

# A. Plot original waveform
plt.subplot(2, 2, 1)
plt.plot(samples, color='purple')
plt.title("📈 Original Audio Waveform")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")

# B. Frequency histogram
plt.subplot(2, 2, 2)
plt.hist(samples, bins=50, color='orange')
plt.title("📊 Amplitude Frequency Histogram")
plt.xlabel("Amplitude")
plt.ylabel("Count")

# C. Bitstream size comparison
original_bits = len(samples) * 8
compressed_bits = len(encoded_bits)
plt.subplot(2, 1, 2)
plt.bar(["Original", "Compressed"], [original_bits, compressed_bits], color=["blue", "green"])
plt.title("🧠 Huffman Compression Stats")
plt.ylabel("Total Bits")

plt.tight_layout()
plt.show()

print(f"\n🔢 Original: {original_bits} bits | Compressed: {compressed_bits} bits | Compression: {(compressed_bits/original_bits)*100:.2f}%")
