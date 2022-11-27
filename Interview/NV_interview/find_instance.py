import math

import numpy as np


def find_instance(mask: np.ndarray):
    """
    mask: of size [m, n]
    """
    index = {}
    instance_id = 0
    if mask[0][0] == 1:
        index[(0, 0)] = instance_id
        instance_id += 1
    m, n = mask.shape
    for i in range(1, m):
        for j in range(1, n):
            if mask[i][j] == 1:
                if mask[i - 1][j] in index:



if __name__ == "__main__":
    pass


