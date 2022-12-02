import math
from typing import List

import numpy as np
from loguru import logger


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            sub_problem_ans = [dp[i - c] for c in coins if i - c >= 0 and dp[i - c] is not None]
            if sub_problem_ans:
                dp[i] = 1 + min(sub_problem_ans)
        
        if dp[amount] is None:
            return -1

        return dp[amount]


if __name__ == '__main__':
    assert Solution().coinChange([1,2,5], 11) == 3
    assert Solution().coinChange([1,2,5], 10) == 2
    assert Solution().coinChange([1], 10) == 10
    assert Solution().coinChange([3], 10) == -1
    assert Solution().coinChange([4, 1, 8], 10) == 3
    assert Solution().coinChange([2], 3) == -1
    assert Solution().coinChange([1], 0) == 0
