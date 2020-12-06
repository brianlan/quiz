from typing import List
import numpy as np
from loguru import logger


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        if k == 0:
            return 0
        hold = [[-99999999] * (n + 1) for _ in range(k)]
        empty = [[-99999999] * (n + 1) for _ in range(k)]
        hold[0][0] = -prices[0]
        empty[0][0] = 0

        prices = [None] + prices  # make it the same length as hold and empty
        for i in range(1, n + 1):
            for j in range(k):
                if j == 0:
                    hold[j][i] = max(-prices[i], hold[0][i - 1])
                else:
                    hold[j][i] = max(empty[j - 1][i - 1] - prices[i], hold[j][i - 1])
                
                empty[j][i] = max(hold[j][i - 1] + prices[i], empty[j][i - 1])

        logger.debug(k)
        logger.debug(prices)
        logger.debug(f"\n{np.array(hold)}")
        logger.debug(f"\n{np.array(empty)}")

        return max(0, max([h[-1] for h in hold]), max([e[-1] for e in empty]))


if __name__ == "__main__":
    # input = 2, [3,2,6,5,0,3]
    # input = 2, [2,4,1]
    input = 2, [3,3,5,0,0,3,1,4]
    # input = 4, [1, 0, 3, 5, 0, 5, 7, 19, 12, 2]
    # input = np.random.randint(5), np.random.randint(20, size=10).tolist()
    logger.info(Solution().maxProfit(*input))