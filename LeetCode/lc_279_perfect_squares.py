import math

from common import *


class Solution:
    """DP
    重要公式：
    numSquares(n) = min(numSquares(n - k) for all k) + 1
    """
    def numSquares(self, n: int) -> int:
        square_nums = [i * i for i in range(1, int(n ** 0.5) + 1)]
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            possible_k = square_nums[:int(i ** 0.5)]
            dp[i] = 1 + min([dp[i - k] for k in possible_k])
        return dp[-1]

class Solution2:
    """BFS
    重要公式：
    can_get_n_from_c_square_nums(n, c) = can_get_n_from_c_square_nums(n - k, c - 1)
    """
    def numSquares(self, n: int) -> int:
        pass


if __name__ == '__main__':
    logger.debug(f"\n{[Solution().numSquares(i) for i in range(1, 21)]}")
