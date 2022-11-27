import math

import numpy as np


# H <- float, height of heatmap
# W <- float, width of heatmap
# pts <- tensor, shape of [N,2], N keypoints
# radius <- float, radius of key circle
def rasterize_heatmap(H, W, pts, radius):
    margin = math.ceil(2 * radius)
    heatmap = np.zeros((H + margin, W + margin), dtype=np.int32)
    circle = generate_circle_kernel(radius)
    r = circle.shape[0]
    for p in pts:
        x, y = p[0], p[1]
        heatmap[x - r: x + r + 1, y - r: y + r + 1] = heatmap[x - r: x + r + 1, y - r: y + r + 1] + circle
    heatmap = (heatmap > 0).astype(np.int32)
    return heatmap[radius: -radius, radius: -radius]


def generate_circle_kernel(radius: float) -> np.ndarray:
    size = math.ceil(radius * 2) + 1
    circle = np.zeros((size, size), dtype=np.int32)
    center = np.array([radius, radius])
    for i in range(size):
        for j in range(size):
            cur_pt = np.array([i, j])
            circle[i][j] = int(dist(cur_pt, center) <= radius)


def dist(x1: np.ndarray, x2: np.ndarray):
    """
    x1: of size [1, 2]
    x2: of size [1, 2]
    """
    diff = x1 - x2
    diff_sqr = diff * diff
    sqr_sum = diff_sqr.sum()
    _dist = sqr_sum.sqrt()
    return _dist


if __name__ == "__main__":
    pass


