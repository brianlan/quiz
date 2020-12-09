import numpy as np
from loguru import logger


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        logger.debug(f"{m}, {n}")
        if m < 2 or n < 2:
            return 1
        opt = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            opt[i][1] = 1
        for j in range(1, n + 1):
            opt[1][j] = 1
        logger.debug(f"\n{np.array(opt)}")
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                opt[i][j] = opt[i][j - 1] + opt[i - 1][j]
        logger.debug(f"\n{np.array(opt)}")
        return opt[-1][-1]


if __name__ == "__main__":
    print(Solution().uniquePaths(3, 7))