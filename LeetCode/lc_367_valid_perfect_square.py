from common import *


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # logger.debug(f"{num}")
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            # logger.debug(f"\n{mid}")
            sqr = mid * mid
            if sqr > num:
                r = mid - 1
            elif sqr < num:
                l = mid + 1
            else:
                return True

        return False


if __name__ == '__main__':
    nums = np.arange(1024) + 1
    for num in nums:
        # num = 25
        is_perfect_sqr = Solution().isPerfectSquare(num)
        gt = np.abs(np.sqrt(num) - np.round(np.sqrt(num))) < 1e-6
        assert is_perfect_sqr == gt, f"test failed for num: {num} ({is_perfect_sqr=}, {gt=})"
