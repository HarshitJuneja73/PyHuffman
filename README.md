# PyHuffman
# Huffman Compression and Decompression GUI

This project implements a simple GUI application for Huffman compression and decompression using the tkinter library in Python.

## Description

The Huffman algorithm is a widely used lossless data compression technique that assigns variable-length codes to input characters based on their frequencies. Characters with higher frequencies are assigned shorter codes, resulting in efficient compression.

## Data Structures

1. **BinaryTree**: The `BinaryTree` class is used to create nodes for the Huffman binary tree. These nodes represent characters and their frequencies. The binary tree is used to build the Huffman codes during compression and decoding during decompression.

2. **Min Heap (Priority Queue)**: The Huffman algorithm requires maintaining a min heap to efficiently find the two nodes with the minimum frequencies during the construction of the Huffman tree. Python's built-in `heapq` module is used to implement the min heap.

3. **Map (Dictionary)**: A dictionary is used to store the Huffman codes for each character during compression and their reverse mappings during decompression. This allows for efficient encoding and decoding of the input text.

## Algorithms

1. **Huffman Compression**: The `Huffmancode` class implements the Huffman compression algorithm. The steps involved in compression are as follows:
   - Calculate the frequency of each character in the input text.
   - Build a min heap of nodes representing characters and their frequencies.
   - Construct a Huffman binary tree by merging the two nodes with the minimum frequencies from the min heap.
   - Generate Huffman codes for each character based on their position in the Huffman tree.
   - Encode the input text using the generated Huffman codes and pad it to ensure the encoded text's length is a multiple of 8.
   - Write the compressed binary data to a new file.

2. **Huffman Decompression**: The `Huffmancode` class also implements the Huffman decompression algorithm. The steps involved in decompression are as follows:
   - Read the compressed binary data from the file.
   - Remove padding and extract the encoded text.
   - Traverse the Huffman binary tree using the encoded text to decode the original input text.
   - Write the decompressed text to a new file.

## How to Use

1. Run the `main.py` file.
2. Click the "Compress File" button to select a file for compression.
3. The compressed file will be saved with the extension `.bin`.
4. Click the "Decompress File" button to select a compressed file for decompression.
5. The decompressed file will be saved with the suffix `_decompressed.txt`.

## Requirements

- Python 3.x
- tkinter library (usually included with Python)

