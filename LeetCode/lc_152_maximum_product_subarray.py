from common import *
import operator


class Solution:
    def __init__(self):
        self.candidates = []

    def calc_max_product(self, nums):
        n = len(nums)
        if n == 0:
            return -inf
        if n == 1:
            return nums[0]
        preprod = list(accumulate(nums, func=operator.mul))
        # logger.debug(f"\n{preprod}")
        first_neg_num = -inf
        for i in preprod:
            if i < 0:
                first_neg_num = i
                break
        return max(max(preprod), min(preprod) // first_neg_num)

    def maxProduct(self, nums: List[int]) -> int:
        # logger.debug(f"\n{nums}")
        n = len(nums)
        if n == 1:
            return nums[0]
        if 0 in nums:
            self.candidates.append(0)
        l, r = 0, 1
        while r <= n:
            if nums[r - 1] == 0:  # split here
                self.candidates.append(self.calc_max_product(nums[l:r-1]))
                l = r
            r += 1
        self.candidates.append(self.calc_max_product(nums[l:r]))
        return max(self.candidates)


class Solution2:
    """DP"""
    def maxProduct(self, nums: List[int]) -> int:
        # logger.debug(f"\n{nums}")
        n = len(nums)
        if n == 1:
            return nums[0]
        dp_max = [-inf for i in range(n)]
        dp_min = [inf for i in range(n)]
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1, n):
            candidates = dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i], nums[i]
            dp_min[i] = min(candidates)
            dp_max[i] = max(candidates)
        return max(dp_max)


if __name__ == '__main__':
    for _ in range(100):
        # nums = (np.random.randint(21, size=15) - 10).tolist()
        nums = (np.random.randint(11, size=8) - 5).tolist()
        # nums = [0, -5]
        # nums = [-5, 0]
        # nums = [-8, -7, 7, 5, 1, 4, 7, 4, -7, 10, -6, 4, 2, 4, -5]
        # nums = [3, -1, 2, 5, -4, 5, 1, -2]
        ans1 = Solution().maxProduct(nums)
        ans2 = Solution2().maxProduct(nums)
        assert ans1 == ans2, f"{ans1} != {ans2}"
    # logger.info(Solution().maxProduct(nums))
