"""
https://bhrigu.me/post/huffman-coding-python-implementation/
https://www.geeksforgeeks.org/text-file-compression-and-decompression-using-huffman-coding/
https://deeppatel23.medium.com/text-file-compressor-with-huffman-coding-9d0ddc30440a
https://www.openbookproject.net/py4fun/huffman/huffman.html
"""

import compresor
import descompresor
import verificador
import sys
from compresor import Huffman

path = "LaBiblia.txt"

h = Huffman(path)

output_path = h.compress()

decom_path = h.decompress(output_path)
