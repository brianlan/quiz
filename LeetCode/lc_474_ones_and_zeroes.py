from common import *

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """解题思路：
        建模成0-1 knapsack problem （0-1 背包问题）
        strs中的每个二进制字符串的value都为1，cost分为“0”的cost和“1”的cost
        最终就是要求满足背包大小(m, n)情形下，最大的value
        """
        s = len(strs)
        values = [1] * s
        ints = [[int(i) for i in st] for st in strs]
        costs = [(len(it)-sum(it), sum(it)) for it in ints]
        logger.debug(f"\n{strs=}\n{costs=}")
        dp = [[[-inf] * (n + 1) for i in range(m + 1)] for i in range(s + 1)]
        for j in range(m + 1):
            for k in range(n + 1):
                dp[0][j][k] = 0
        logger.debug(f"\n{np.array(dp[0])}")
        for i in range(1, s + 1):
            c0, c1, v = *costs[i - 1], values[i - 1]
            for j in range(m + 1):
                for k in range(n + 1):
                    if c0 <= j and c1 <= k:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][max(0, j - c0)][max(0, k - c1)] + v)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
            logger.debug(f"\n{strs[i - 1]}, {costs[i - 1]}\n{np.array(dp[i])}")
        return dp[-1][-1][-1]


if __name__ == "__main__":
    strs, m, n = ["10", "0001", "111001", "1", "0"], 5, 3
    # strs, m, n = ["10", "0", "1"], 1, 1
    # strs, m, n = ["0"], 1, 1
    logger.info(Solution().findMaxForm(strs, m, n))
