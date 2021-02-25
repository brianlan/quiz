from common import *


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        Based on code from Leetcode 583
        """
        n1, n2 = len(s1), len(s2)
        if n1 == 0:
            return sum([ord(c) for c in s2])
        if n2 == 0:
            return sum([ord(c) for c in s1])
        
        logger.debug(f"\ns1: {s1}({[ord(s) for s in s1]})\ns2: {s2}({[ord(s) for s in s2]})")
        
        dp = [[inf] * (n2 + 1) for i in range(n1 + 1)]
        asc = [[0] * (n2 + 1) for i in range(n1 + 1)]

        cumsum = 0
        dp[0][0] = asc[0][0] = 0
        for i in range(1, n1 + 1):
            dp[i][0] = i
            cumsum += ord(s1[i - 1])
            asc[i][0] = cumsum
        
        cumsum = 0
        for j in range(1, n2 + 1):
            dp[0][j] = j
            cumsum += ord(s2[j - 1])
            asc[0][j] = cumsum

        # logger.debug(f"\n{np.array(dp)}")
        for i in range(1, n1 + 1):
            c1 = s1[i - 1]
            for j in range(1, n2 + 1):
                c2 = s2[j - 1]
                if c1 == c2:
                    dp[i][j] = dp[i - 1][j - 1]
                    asc[i][j] = asc[i - 1][j - 1]
                else:
                    if dp[i - 1][j] > dp[i][j - 1]:
                        dp[i][j] = 1 + dp[i][j - 1]
                        asc[i][j] = ord(c2) + asc[i][j - 1]
                    elif dp[i - 1][j] < dp[i][j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j]
                        asc[i][j] = ord(c1) + asc[i - 1][j]
                    else:
                        dp[i][j] = 1 + dp[i - 1][j]
                        asc[i][j] = min(
                            ord(c1) + asc[i - 1][j],
                            ord(c2) + asc[i][j - 1],
                        )
        logger.debug(f"\n{np.array(dp)}")
        logger.debug(f"\n{np.array(asc)}")

        return asc[-1][-1]


class Solution2:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        Only use ascii value as the value we're going to optimize.
        要基于一个结论：少删一个字符，一定会使总体ascii和更小。
        """
        n1, n2 = len(s1), len(s2)
        if n1 == 0:
            return sum([ord(c) for c in s2])
        if n2 == 0:
            return sum([ord(c) for c in s1])
        
        logger.debug(f"\ns1: {s1}({[ord(s) for s in s1]})\ns2: {s2}({[ord(s) for s in s2]})")
        
        asc = [[0] * (n2 + 1) for i in range(n1 + 1)]

        cumsum = 0
        for i in range(1, n1 + 1):
            cumsum += ord(s1[i - 1])
            asc[i][0] = cumsum
        
        cumsum = 0
        for j in range(1, n2 + 1):
            cumsum += ord(s2[j - 1])
            asc[0][j] = cumsum

        for i in range(1, n1 + 1):
            c1 = s1[i - 1]
            for j in range(1, n2 + 1):
                c2 = s2[j - 1]
                if c1 == c2:
                    asc[i][j] = asc[i - 1][j - 1]
                else:
                    asc[i][j] = min(
                        ord(c1) + asc[i - 1][j],
                        ord(c2) + asc[i][j - 1],
                    )
        logger.debug(f"\n{np.array(asc)}")

        return asc[-1][-1]



if __name__ == "__main__":
    # s1 = "sea"
    # s2 = "eat"
    # s1 = "delete"
    # s2 = "leet"
    s1 = "".join([chr(97 + i) for i in np.random.randint(26, size=100)])
    s2 = "".join([chr(97 + j) for j in np.random.randint(26, size=20)])
    logger.info(Solution2().minimumDeleteSum(s1, s2))
