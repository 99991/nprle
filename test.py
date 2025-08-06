import numpy as np
from nprle import (
    rle_encode,
    rle_decode,
    rle_intersect,
    rle_union,
    rle_difference,
    rle_symmetric_difference,
    rle_miou,
    rle_area,
)

def test_random_1d():
    for seed in range(100):
        np.random.seed(seed)
        n = np.random.randint(10)
        shape = (n,)

        values1 = np.random.rand(n) > 0.5
        values2 = np.random.rand(n) > 0.5

        test_values(values1, values2, shape)

def numpy_miou(mask1, mask2):
    numerator = np.sum(mask1 & mask2)

    if numerator == 0:
        return 0.0

    return numerator / np.sum(mask1 | mask2)

def test_values(values1, values2, shape):
    encoded1 = rle_encode(values1)
    encoded2 = rle_encode(values2)

    expected_miou = numpy_miou(values1, values2)
    miou = rle_miou(encoded1, encoded2)

    # mIoU will be exactly equal without rounding error
    assert miou == expected_miou
    assert np.sum(values1 & values2) == rle_area(rle_intersect(encoded1, encoded2))
    assert np.sum(values1 | values2) == rle_area(rle_union(encoded1, encoded2))
    assert np.sum(values1 & ~values2) == rle_area(rle_difference(encoded1, encoded2))
    assert np.sum(values1 ^ values2) == rle_area(rle_symmetric_difference(encoded1, encoded2))
    assert np.array_equal(values1, rle_decode(encoded1, shape))
    assert np.array_equal(values2, rle_decode(encoded2, shape))

def make_circles(shape):
    h, w = shape
    y, x = np.ogrid[:h, :w]

    cx1 = w // 3
    cy1 = h // 2

    r1 = w // 4

    cx2 = 2 * w // 3
    cy2 = h // 2

    r2 = w // 5

    circle1 = np.hypot(x - cx1, y - cy1) < r1
    circle2 = np.hypot(x - cx2, y - cy2) < r2

    return circle1, circle2

def test_2d_circles():
    w = 640
    h = 480

    shape = (h, w)

    circle1, circle2 = make_circles(shape)

    test_values(circle1, circle2, shape)

if __name__ == "__main__":
    test_random_1d()
    test_2d_circles()
    print("Tests passed :)")
