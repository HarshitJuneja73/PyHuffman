import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from huffman import Huffmancode

class HuffmanApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Huffman Compression and Decompression")
        self.geometry("400x200")
        self.file_path = ""

        # Compress Button
        compress_btn = tk.Button(
            self, text="Compress File", command=self.compress_file)
        compress_btn.pack(pady=10)

        # Decompress Button
        decompress_btn = tk.Button(
            self, text="Decompress File", command=self.decompress_file)
        decompress_btn.pack(pady=10)

    def browse_file(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("Binary Files", "*.bin")])

    def compress_file(self):
        self.browse_file()
        if not self.file_path:
            return

        try:
            huffman = Huffmancode(self.file_path)
            compressed_file = huffman.compression()
            messagebox.showinfo(
                "Compression", "File compressed successfully!\nSaved as: " + compressed_file)
        except Exception as e:
            messagebox.showerror("Compression Error", str(e))

    def decompress_file(self):
        self.browse_file()
        if not self.file_path:
            return

        try:
            huffman = Huffmancode(self.file_path)
            decompressed_file = huffman.decompressed(self.file_path)
            messagebox.showinfo(
                "Decompression", "File decompressed successfully!\nSaved as: " + decompressed_file)
        except Exception as e:
            messagebox.showerror("Decompression Error", str(e))


if __name__ == "__main__":
    app = HuffmanApp()
    app.mainloop()

