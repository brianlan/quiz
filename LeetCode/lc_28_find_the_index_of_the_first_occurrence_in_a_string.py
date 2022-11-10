import math

import numpy as np
from loguru import logger


class Solution:
    """This solution implements Sunday Algorithm"""
    def strStr(self, haystack: str, needle: str) -> int:
        n_text, n_pat = len(haystack), len(needle)
        if n_pat > n_text or n_text == 0 or n_pat == 0:
            return -1
        i = 0

        cache = {c: 0 for c in needle}
        _ = {cache.update({needle[i]: i}) for i in range(n_pat)}

        while i <= n_text - n_pat:
            for j in range(n_pat):
                if haystack[i + j] != needle[j]:
                    if i + n_pat >= n_text:
                        return -1

                    if haystack[i + n_pat] not in cache:
                        i += n_pat + 1
                    else:
                        idx = cache[haystack[i + n_pat]]
                        i += n_pat - idx
                    break
            else:
                return i
        
        return -1
                    



if __name__ == '__main__':
    assert Solution().strStr("sadbutsad", "sad") == 0
    assert Solution().strStr("leetcode", "leeto") == -1
    assert Solution().strStr("BBC ABCDAB ABCDABCDABDE", "ABCDABD") == 15
    assert Solution().strStr("bbbbbab", "bbab") == 3
    assert Solution().strStr("bbbbbac", "bbab") == -1
    assert Solution().strStr("cazzbzzayabaayaxybbcxzabzbxcxxa", "xcccab") == -1
    assert Solution().strStr("acdcbdbcaaacdaccccacdaadadadcdbd", "ccacd") == 16

