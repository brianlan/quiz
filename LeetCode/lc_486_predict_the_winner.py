from typing import List
from loguru import logger
import numpy as np


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        logger.debug(nums)
        n = len(nums)
        if n <= 2:
            return True
        d = [[0] * n for _ in range(n)]
        for i in range(n):
            d[i][i] = nums[i]
        for span in range(1, n):
            for i in range(n - span):
                j = i + span
                print(i, j)
                d[i][j] = max(-d[i+1][j] + nums[i], -d[i][j - 1] + nums[j])
        logger.debug(f"\n{np.array(d)}")
        return d[0][-1] >= 0


if __name__ == "__main__":
    # nums = (np.random.randint(10, size=5) + 1).tolist()
    nums = [1, 9, 4, 1, 10]
    # nums = [1, 5, 233, 7]
    logger.info(Solution().PredictTheWinner(nums))