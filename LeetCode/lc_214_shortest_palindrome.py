import math
from collections import defaultdict

import numpy as np
from loguru import logger


class Solution:
    # @profile
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        i, j = 0, n - 1
        lcache = set()
        num_matched = 0
        num_abandon = 0
        while i != j and i < j and i < n and j >= 0:
            if s[i] == s[j]:
                num_matched += 1
                i += 1
            else:
                lcur = s[i-num_matched:i]
                rcur_reversed = ''.join(reversed(s[j:j+num_matched]))
                p = 0
                while p < num_matched and lcur[:num_matched-p] != rcur_reversed[p:]:
                    p += 1
                i -= p
                num_matched -= p
                num_abandon += p + 1

            j -= 1
        if num_abandon == 0:
            return s
        return ''.join(reversed(s[-num_abandon:])) + s


class Solution_hard_to_implement:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        i = (n - 1) // 2
        j = 0
        cache = defaultdict(list)
        while i > 0:
            while i - j > 0:
                if s[i - (j + 1)] == s[i + (j + 1)]:
                    for k in range(1, j + 1):
                        cache[k].append((i - (k + 1), i - (k - 1), s[i - (k + 1)] == s[i - (k - 1)]))
                    j += 1
                else:
                    for k in range(1, j + 1):
                        if all(match[2] for match in cache[k][-1]):
                            i -= k
                            j = j - k + 1
                            for h in range(1, j + 1):
                                if h < k:
                                    del cache[h]
                                else:
                                    cache[h] = [(t[0] - k, t[1] - k, t[2]) for t in cache[h][:-k]]
                            break
                    else:
                        i -= j
                        j = 0
                        cache = defaultdict(list)

            if i - j == 0:
                return "success"

            i += 1


def generate_quiz(n=50000, k=4, seed=42):
    np.random.seed(seed)
    return ''.join([chr(ord('a') + i) for i in np.random.randint(0, k, size=n)])


if __name__ == '__main__':
    # for _ in range(10):
    #     quiz = generate_quiz()
    #     Solution().shortestPalindrome(quiz)
    assert Solution().shortestPalindrome("b") == "b"
    assert Solution().shortestPalindrome("bb") == "bb"
    assert Solution().shortestPalindrome("bbb") == "bbb"
    assert Solution().shortestPalindrome("bcb") == "bcb"
    assert Solution().shortestPalindrome("aacecaaa") == "aaacecaaa"
    assert Solution().shortestPalindrome("abcd") == "dcbabcd"
    assert Solution().shortestPalindrome("baaaaababaabaebca") == "acbeabaababaaaaababaabaebca"
    assert Solution().shortestPalindrome("babbcbbeeebbbab") == "babbbeeebbcbbabbcbbeeebbbab"
    assert Solution().shortestPalindrome("bbbbcbbeeebbbbb") == "bbbbbeeebbcbbbbcbbeeebbbbb"
    assert Solution().shortestPalindrome("babacbbeeebabab") == "bababeeebbcababacbbeeebabab"
