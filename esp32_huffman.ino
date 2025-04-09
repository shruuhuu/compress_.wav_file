#include <Arduino.h>

#define MAX_BYTES 256
uint8_t wavData[MAX_BYTES];
int freq[256] = {0};

struct Node {
  uint8_t data;
  int freq;
  Node* left;
  Node* right;
};

#define MAX_NODES 256
Node nodes[MAX_NODES];
int nodeCount = 0;

Node* createNode(uint8_t data, int freq) {
  Node* n = &nodes[nodeCount++];
  n->data = data;
  n->freq = freq;
  n->left = n->right = NULL;
  return n;
}

Node* queue[MAX_NODES];
int queueSize = 0;

void push(Node* n) {
  queue[queueSize++] = n;
}

Node* popMin() {
  int minIndex = 0;
  for (int i = 1; i < queueSize; i++) {
    if (queue[i]->freq < queue[minIndex]->freq) {
      minIndex = i;
    }
  }
  Node* minNode = queue[minIndex];
  for (int i = minIndex; i < queueSize - 1; i++) {
    queue[i] = queue[i + 1];
  }
  queueSize--;
  return minNode;
}

Node* buildTree() {
  for (int i = 0; i < 256; i++) {
    if (freq[i] > 0) {
      push(createNode(i, freq[i]));
    }
  }
  while (queueSize > 1) {
    Node* left = popMin();
    Node* right = popMin();
    Node* parent = createNode(0, left->freq + right->freq);
    parent->left = left;
    parent->right = right;
    push(parent);
  }
  return popMin();
}

String codes[256];

void generateCodes(Node* root, String code) {
  if (!root) return;
  if (!root->left && !root->right) {
    codes[root->data] = code;
  }
  generateCodes(root->left, code + "0");
  generateCodes(root->right, code + "1");
}

String encodeWav() {
  String encoded = "";
  for (int i = 0; i < MAX_BYTES; i++) {
    encoded += codes[wavData[i]];
  }
  return encoded;
}

void setup() {
  Serial.begin(115200);
  delay(3000);
  Serial.println("ESP32 Ready for WAV data...");
}

bool received = false;
int byteCount = 0;

void loop() {
  if (!received && Serial.available()) {
    while (Serial.available() && byteCount < MAX_BYTES) {
      wavData[byteCount++] = Serial.read();
    }

    if (byteCount == MAX_BYTES) {
      received = true;

      Serial.println("🎧 Received WAV samples:");
      for (int i = 0; i < MAX_BYTES; i++) {
        freq[wavData[i]]++;
      }

      nodeCount = 0;
      queueSize = 0;
      Node* root = buildTree();
      generateCodes(root, "");

      Serial.println("📦 Codebook:");
      for (int i = 0; i < 256; i++) {
        if (codes[i].length() > 0) {
          Serial.print(i);
          Serial.print(": ");
          Serial.println(codes[i]);
        }
      }

      String compressed = encodeWav();
      Serial.println("🔒 Huffman Encoded Output (first 200 bits):");
      Serial.println(compressed.substring(0, 200));

      Serial.print("Original bits: ");
      Serial.println(MAX_BYTES * 8);
      Serial.print("Compressed bits: ");
      Serial.println(compressed.length());
    }
  }
}
