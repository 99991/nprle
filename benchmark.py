from nprle import rle_encode, rle_intersect, rle_area, rle_miou
from collections import defaultdict
from test import make_circles, numpy_miou
import matplotlib.pyplot as plt
import numpy as np
import time

class Timer:
    def __init__(self):
        self.times = defaultdict(lambda: defaultdict(list))
        self.start_time = time.perf_counter()

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self, size, name):
        end_time = time.perf_counter()

        elapsed_time = end_time - self.start_time

        self.times[name][size].append(elapsed_time)

        self.start_time = time.perf_counter()

def test():
    sizes = np.geomspace(128, 4096, 6).round().astype(int)

    t = Timer()

    for size in sizes:
        shape = (size, size)
        print(f"Testing size {size}")

        circle1, circle2 = make_circles(shape)

        # Run a few times to get stable results 🐴
        for _ in range(10):
            t.start()

            circle1_counts = rle_encode(circle1)

            t.stop(size, "rle_encode mask1")

            circle2_counts = rle_encode(circle2)

            t.stop(size, "rle_encode mask2")

            intersection = rle_intersect(circle1_counts, circle2_counts)

            t.stop(size, "rle_intersect")

            rle_area(intersection)

            t.stop(size, "rle_area")

            iou1 = rle_miou(circle1_counts, circle2_counts)

            t.stop(size, "rle_miou")

            iou2 = numpy_miou(circle1, circle2)

            t.stop(size, "NumPy mIoU")

            assert iou1 == iou2

    plt.figure(figsize=(10, 6))
    # Don't convert text to paths
    plt.rcParams["svg.fonttype"] = "none"
    for name, size_times in t.times.items():
        sizes = sorted(size_times)
        times = [min(size_times[size]) for size in sizes]
        plt.loglog(sizes, times, label=name)
    plt.legend()
    plt.xlabel("Image size")
    plt.ylabel("Time [seconds]")
    plt.xticks(sizes, [f"{size}x{size}" for size in sizes])
    plt.tight_layout()
    plt.savefig("benchmark.png", bbox_inches="tight", pad_inches=0.1)
    plt.show()

if __name__ == "__main__":
    test()
