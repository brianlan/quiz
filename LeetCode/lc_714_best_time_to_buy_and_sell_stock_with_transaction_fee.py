from typing import List
import numpy as np
from loguru import logger


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        hold = [0] * (n + 1)
        empty = [0] * (n + 1)
        hold[0] = -prices[0]
        for i in range(1, n + 1):
            hold[i] = max(empty[i - 1] - prices[i - 1], hold[i - 1])
            # if hold[i - 1] + prices[i - 1] > empty[i - 1]:
            empty[i] = max(hold[i - 1] + prices[i - 1] - fee, empty[i - 1])
        logger.debug(prices)
        logger.debug(fee)
        logger.debug(f"\n{np.array([hold, empty])}")
        return max(0, hold[-1], empty[-1])


if __name__ == "__main__":
    # input = [7,6,4,3,1]
    # input = [1, 3, 2, 8, 4, 9], 2
    input = np.random.randint(20, size=10).tolist(), np.random.randint(5)
    logger.info(Solution().maxProfit(*input))