from functools import lru_cache
import time


class Solution:
    def __init__(self):
        self.longest = ""

    @lru_cache(maxsize=None)
    def is_palindrome(self, s, i, j):
        if i == j:
            return True
        if j == i + 1:
            return s[i] == s[j]
        return self.is_palindrome(s, i + 1, j - 1) and s[i] == s[j]

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n] * n
        for i in range(n):
            for j in range(i, n):
                dp[i][j] = _is_palindrome = self.is_palindrome(s, i, j)
                if _is_palindrome and j - i + 1 > len(self.longest):
                    self.longest = s[i : j + 1]
        return self.longest


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans


if __name__ == "__main__":
    t0 = time.time()
    # print(Solution().longestPalindrome("abbabba"))
    # print(Solution().longestPalindrome("abbabbca"))
    print(
        Solution().longestPalindrome(
            "lejyqjcpluiggwlmnumqpxljlcwdsirzwlygexejhvojztcztectzrepsvwssiixfmpbzshpilmojehqyqpzdylxptsbvkgatzdlzphohntysrbrcdgeaiypmaaqilthipjbckkfbxtkreohabrjpmelxidlwdajmkndsdbbaypcemrwlhwbwaljacijjmsaqembgtdcskejplifnuztlmvasbqcyzmvczpkimpbbwxdtviptzaenkbddaauyvqppagvqfpednnckooxzcpuudckakutqyknuqrxjgfdtsxsoztjkqvfvelrklforpjnrbvyyvxigjhkjmxcphjzzilvbjbvwiwnnkbmboiqamgoimujtswdqesighoxsprhnsceshotakvmoxqkqjvbpqucvafiuqwmrlfjpjijbctfupywkbawquchbclgvhxbanybret"
        )
    )
    print(f"Time elapsed: {time.time() - t0:.2f}s")