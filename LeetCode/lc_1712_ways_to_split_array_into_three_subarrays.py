from common import *
import bisect

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        num_ways = 0
        cumsum = list(accumulate(nums))
        tot = cumsum[-1]
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                l, m, r = cumsum[i], cumsum[j] - cumsum[i], tot - cumsum[j]
                if l <= m <= r:
                    num_ways += 1
                else:
                    if m > r:
                        break
            if l > m > r:
                break
                    # print(i, j, nums[:i+1], nums[i+1:j+1], nums[j+1:])
        return num_ways


class Solution2:
    """Bisection, O(NlogN)"""
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        cumsum = list(accumulate(nums))
        tot = cumsum[-1]
        num_ways = 0
        r = 1
        for l in range(0, n - 2):
            r = max(r, l + 1)
            while r < n - 2 and cumsum[r] - cumsum[l] < cumsum[l]:
                r += 1
            lo, hi = r, n - 2
            md = r
            if cumsum[l] <= cumsum[r] - cumsum[l] <= tot - cumsum[r]:
                while True:
                    _md = (lo + hi) // 2
                    if tot - cumsum[_md] >= cumsum[_md] - cumsum[l]:
                        lo = _md + 1
                        md = _md
                    else:
                        hi = _md - 1
                    if lo > hi:
                        break
                num_ways += md - r + 1
        num_ways %= 1000000007
        return num_ways


if __name__ == "__main__":
    # nums = np.random.randint(20, size=100).tolist()
    # nums = [1, 2, 0, 1, 1, 5, 2, 2, 4, 9]  # 19
    # nums = [6, 6, 3, 7, 6, 8, 6, 6, 5, 1]  # 5
    # nums = [7, 4, 2, 2, 4, 7, 3, 7, 9, 1]  # 6
    # nums = [1,1,1]  # 1
    # nums = [1,2,2,2,5,0]  # 3
    nums = [0] * 5
    logger.debug(nums)
    logger.info(Solution2().waysToSplit(nums))
