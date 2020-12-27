from common import *

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        h = len(s) // 2
        ls = s.lower()
        a, b = Counter(ls[:h]), Counter(ls[h:])
        letters = 'aeiou'
        return sum([a[l] for l in letters]) == sum([b[l] for l in letters])

if __name__ == "__main__":
    s = "book"
    logger.info(Solution().halvesAreAlike(s))