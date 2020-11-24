from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """ opt[i] = max(opt[i - 1], opt[i - 2] + nums[i]) """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        opt = [0] * (n + 1)
        opt[1] = nums[0]
        for i in range(2, n + 1):
            opt[i] = max(opt[i - 1], opt[i - 2] + nums[i - 1])
        return opt[n]


if __name__ == "__main__":
    print(Solution().rob([2, 7, 9, 3, 1]))
    print(Solution().rob([2, 1, 3, 4, 1, 5, 3, 2, 3, 9]))
