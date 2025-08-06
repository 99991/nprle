from PIL import Image
import numpy as np
from nprle import rle_encode, rle_decode, rle_miou, rle_intersect, rle_area

# Load binary masks as NumPy arrays
mask1 = np.array(Image.open("data/binary_mask1.png"))
mask2 = np.array(Image.open("data/binary_mask2.png"))

# Run-length-encode binary masks count number of consecutive 0 and 1 bits
counts1 = rle_encode(mask1)
counts2 = rle_encode(mask2)

shape = mask1.shape

print(f"mask1 of shape {shape} requires {mask1.nbytes/1000:.1f} KB using {mask1.dtype}.")

# Run-length encoding can save a lot of memory (97 % in this case)
percent = 100 * counts1.nbytes / mask1.nbytes
print(f"counts1 only requires {counts1.nbytes/1000:.1f} KB ({100 - percent:.0f} % reduction) using {counts1.dtype}.")

# Decoding example
mask1_decoded = rle_decode(counts1, shape)
mask2_decoded = rle_decode(counts2, shape)

assert np.array_equal(mask1, mask1_decoded)
assert np.array_equal(mask2, mask2_decoded)

# Computing mean intersection over union using run-length-encoding is very fast
miou = rle_miou(counts1, counts2)

print(f"mIoU (mean intersection over union) of both masks is {miou*100:.1f} %")

intersection = rle_intersect(counts1, counts2)

num_overlapping_pixels = rle_area(intersection)

print(f"{num_overlapping_pixels} pixels are equal to 1 in both masks at once.")
