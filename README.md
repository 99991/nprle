# nprle

`nprle` is a library for run-length-encoding binary masks.

A run-length encoding of a binary mask is a compact representation that
stores the counts of consecutive 0s and 1s in the mask.

For example, the binary mask

```
00 111 0000
```

would be encoded as

```
[2, 3, 4]
```

because it has 2 consecutive 0s, followed by 3 consecutive 1s, and then 4 consecutive 0s.

This representation reduces memory usage and speeds up operations like mean intersection over union (mIoU)
or binary operations (intersection/union/difference/xor),
which can be performed directly on the run-length-encoded masks.

All functions are vectorized with NumPy for better performance.

This library aims to be compatible with the masks from the [COCO dataset](https://cocodataset.org), which is why images use column-major order (configurable).

# Download and run example

```bash
pip install numpy pillow
git clone https://github.com/99991/nprle.git
cd nprle
python test.py
python example.py
```

# Example

```python
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
```

# Benchmark

For larger images, the advantage of using run-length-encoding becomes more pronounced
when compared to traditional pixel-wise operations. The following graph shows the
performance of various operations in relation to increasing image sizes.

Since run-length-encoding is relatively costly (still cheap though), it is recommended to store binary masks in this format so that encoding only needs to be done once.

<img width="985" height="590" alt="benchmark" src="https://github.com/user-attachments/assets/d713868f-a53d-4428-9fed-03867ef15366" />
