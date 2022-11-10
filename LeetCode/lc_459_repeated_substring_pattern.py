from typing import List
import math

import numpy as np
from loguru import logger


class Solution:
    @staticmethod
    def find_factors(n: int) -> List[int]:
        factors = [1]
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                factors += [i, int(n // i)]
        factors += [n]
        return factors

    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False
        factors = self.find_factors(len(s))[:-1]
        for f in factors:
            for i in range(0, len(s), f):
                if s[i:i+f] != s[:f]:
                    break
            else:
                return True
        
        return False

if __name__ == '__main__':
    assert set(Solution.find_factors(10)) == {1, 2, 5, 10}
    assert set(Solution.find_factors(12)) == {1, 2, 3, 4, 6, 12}
    assert set(Solution.find_factors(39)) == {1, 3, 13, 39}
    assert set(Solution.find_factors(7)) == {1, 7}
    assert Solution().repeatedSubstringPattern("abab") is True
    assert Solution().repeatedSubstringPattern("aba") is False
    assert Solution().repeatedSubstringPattern("abcabcabcabc") is True
    assert Solution().repeatedSubstringPattern("a") is False
    assert Solution().repeatedSubstringPattern("bb") is True
    assert Solution().repeatedSubstringPattern("abc") is False
    assert Solution().repeatedSubstringPattern("abcddcbaabcd") is False
    assert Solution().repeatedSubstringPattern("abcdefgabcdefg") is True

