import numpy as np

def rle_encode(values, dtype=np.int32, order="F"):
    # Convert binary values to run-length-encoding.

    if len(values) == 0:
        return np.zeros(0, dtype=dtype)

    # Flatten array in column-major order and ensure boolean type.
    # Use Fortran (column-major) order to be compatible with MSCOCO
    values = np.asarray(values, dtype=bool).ravel(order=order)
    # Pad start and end to detect changes
    values = np.concatenate([[0], values, [~values[-1]]])
    # Find where value changes occur
    changes = values[1:] != values[:-1]
    indices = np.append(0, np.where(changes)[0])
    # Calculate run lengths
    counts = indices[1:] - indices[:-1]
    return counts.astype(dtype)

def rle_decode(counts, shape, order="F"):
    # Decode run-length encoding counts to binary array.

    # Create alternating 0/1 values for each run
    values = np.zeros(len(counts), dtype=bool)
    values[1::2] = 1
    # Repeat values according to run lengths and reshape
    return np.repeat(values, counts).reshape(shape, order=order)

def _rle_merge(counts1, counts2):
    # Combine indices and split for every sign change of either mask.
    indices1 = np.cumsum(counts1)
    indices2 = np.cumsum(counts2)
    indices = np.append(indices1, indices2)
    argsorted = np.argsort(indices)

    is1 = argsorted < len(indices1)
    is2 = ~is1

    values1 = np.cumsum(np.append(0, is1))[:-1] & 1
    values2 = np.cumsum(np.append(0, is2))[:-1] & 1

    counts = np.diff(np.append(0, indices[argsorted]))

    return counts, values1, values2

def _rle_counts_values(counts, values):
    # RLE-encode counts of values.
    # Counts of equal consecutive values are combined.
    if len(counts) == 0:
        return np.zeros(0, dtype=int)

    changes = np.concatenate([[True], values[1:] != values[:-1], [True]])
    indices = np.where(changes)[0]

    sums = np.cumsum(np.append(0, counts))
    counts = sums[indices[1:]] - sums[indices[:-1]]

    return counts

def rle_intersect(counts1, counts2):
    counts, values1, values2 = _rle_merge(counts1, counts2)
    return _rle_counts_values(counts, values1 & values2)

def rle_union(counts1, counts2):
    counts, values1, values2 = _rle_merge(counts1, counts2)
    return _rle_counts_values(counts, values1 | values2)

def rle_difference(counts1, counts2):
    counts, values1, values2 = _rle_merge(counts1, counts2)
    return _rle_counts_values(counts, values1 & ~values2)

def rle_symmetric_difference(counts1, counts2):
    counts, values1, values2 = _rle_merge(counts1, counts2)
    return _rle_counts_values(counts, values1 ^ values2)

def rle_miou(counts1, counts2):
    counts, values1, values2 = _rle_merge(counts1, counts2)

    numerator = np.sum(counts * (values1 & values2))

    if numerator == 0:
        return 0.0

    return numerator / np.sum(counts * (values1 | values2))

def rle_area(encoded):
    return np.sum(encoded[1::2])
