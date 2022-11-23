import math

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


if __name__ == '__main__':
    assert Solution().longestCommonSubsequence("abcde", "a") == 1
    assert Solution().longestCommonSubsequence("g", "ddefg") == 1
    assert Solution().longestCommonSubsequence("abcde", "ace") == 3
    assert Solution().longestCommonSubsequence("abc", "abc") == 3
    assert Solution().longestCommonSubsequence("abc", "def") == 0
