from common import *


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        n1, n2 = len(A), len(B)
        logger.debug(f"\nA: {A}\nB: {B}")
        dp = [[0] * (n2 + 1) for i in range(n1 + 1)]
        for i in range(1, n1 + 1):
            a = A[i - 1]
            for j in range(1, n2 + 1):
                b = B[j - 1]
                if a == b:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        logger.debug(f"\n{np.array(dp)}")
        return dp[-1][-1]
                


if __name__ == "__main__":
    # A = [2, 5, 1, 2, 5]
    # B = [10, 5, 2, 1, 5, 2]
    # A = [1,4,2]
    # B = [1,2,4]
    # A = [1,3,7,1,7,5]
    # B = [1,9,2,5,1]
    # A = [3]
    # B = [3]
    A = (np.random.randint(10, size=20) + 1).tolist()
    B = (np.random.randint(10, size=16) + 1).tolist()
    logger.info(Solution().maxUncrossedLines(A, B))
