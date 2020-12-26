from common import *


class Solution:
    def firstUniqChar(self, s: str) -> int:
        stats = Counter(s)
        candidates = [k for k, v in stats.items() if v == 1]
        if len(candidates) == 0:
            return -1
        return s.index(candidates[0])


if __name__ == "__main__":
    # s = "leetcode"
    s = "loveleetcode"
    logger.info(Solution().firstUniqChar(s))