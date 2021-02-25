from common import *


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        if n1 == 0:
            return n2
        if n2 == 0:
            return n1
        logger.debug(f"\nword1: {word1}\nword2: {word2}")
        dp = [[-inf] * (n2 + 1) for i in range(n1 + 1)]
        for i in range(n1 + 1):
            dp[i][0] = i
        for j in range(n2 + 1):
            dp[0][j] = j
        # logger.debug(f"\n{np.array(dp)}")
        for i in range(1, n1 + 1):
            c1 = word1[i - 1]
            for j in range(1, n2 + 1):
                c2 = word2[j - 1]
                if c1 == c2:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        logger.debug(f"\n{np.array(dp)}")
        return dp[-1][-1]
        

if __name__ == "__main__":
    # word1 = "sea"
    # word2 = "eat"
    # word1, word2 = "d", "abc"
    word1 = "".join([chr(97 + i) for i in np.random.randint(26, size=100)])
    word2 = "".join([chr(97 + j) for j in np.random.randint(26, size=20)])
    logger.info(Solution().minDistance(word1, word2))
