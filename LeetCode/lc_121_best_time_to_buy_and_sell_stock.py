from typing import List
from loguru import logger


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        m = [99999999] * (n + 1)  # stores min value as of position i
        incr = [0] * (n + 1)  # stores the incremental value as of position i
        for i in range(1, n + 1):
            m[i] = min(m[i - 1], prices[i - 1])
            incr[i] = prices[i - 1] - m[i]
        # logger.debug(prices)
        # logger.debug(m[1:])
        # logger.debug(incr[1:])
        return max(incr)


if __name__ == "__main__":
    print(Solution().maxProfit([13, 4, 1, 3, 2, 6, 5, 12, 7, 5, 11]))
