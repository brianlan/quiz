import math
import random
from functools import lru_cache

import numpy as np
from loguru import logger


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + int(text1[i - 1] == text2[j - 1]))
        return dp[-1][-1]


class SolutionBF:
    @lru_cache(maxsize=None)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if m == 0 or n == 0:
            return 0
        return max(
            int(text1[-1] == text2[-1]) + self.longestCommonSubsequence(text1[:-1], text2[:-1]),
            self.longestCommonSubsequence(text1, text2[:-1]),
            self.longestCommonSubsequence(text1[:-1], text2)
        )


if __name__ == '__main__':
    assert SolutionBF().longestCommonSubsequence("deadbfb", "cbdfbfa") == 3
    assert SolutionBF().longestCommonSubsequence("abcde", "a") == 1
    assert SolutionBF().longestCommonSubsequence("g", "ddefg") == 1
    assert SolutionBF().longestCommonSubsequence("abcde", "ace") == 3
    assert SolutionBF().longestCommonSubsequence("abc", "abc") == 3
    assert SolutionBF().longestCommonSubsequence("abc", "def") == 0

    for _ in range(100):
        text1 = ''.join([chr(random.randint(97, 97 + 5)) for _ in range(7)])
        text2 = ''.join([chr(random.randint(97, 97 + 5)) for _ in range(7)])
        try:
            assert Solution().longestCommonSubsequence(text1, text2) == SolutionBF().longestCommonSubsequence(text1, text2)
        except AssertionError:
            logger.debug(text1)
            logger.debug(text2)
            logger.debug(Solution().longestCommonSubsequence(text1, text2))
            logger.debug(SolutionBF().longestCommonSubsequence(text1, text2))
            break
