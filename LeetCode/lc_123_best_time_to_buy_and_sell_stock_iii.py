from typing import List
import numpy as np
from loguru import logger


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        neg_prices = [-p for p in prices]
        Y1 = [-99999999] * n
        N1 = [-99999999] * n
        Y2 = [-99999999] * n
        N2 = [-99999999] * n
        Y1[0] = neg_prices[0]
        for i in range(1, n):
            Y1[i] = max(neg_prices[i], Y1[i - 1])
            N1[i] = max(Y1[i - 1] + prices[i], N1[i - 1])
            Y2[i] = max(N1[i - 1] - prices[i], Y2[i - 1])
            N2[i] = max(Y2[i - 1] + prices[i], N1[i - 1], N2[i - 1])
        logger.debug(prices)
        logger.debug(f"\n{np.array([Y1, N1, Y2, N2])}")
        return max(0, Y1[-1], N1[-1], Y2[-1], N2[-1])


if __name__ == "__main__":
    input = [7,6,4,3,1]
    # input = np.random.randint(20, size=10).tolist()
    logger.info(Solution().maxProfit(input))