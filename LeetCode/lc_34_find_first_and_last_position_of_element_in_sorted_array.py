from typing import List
import numpy as np
from bisect import bisect_right, bisect_left


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        if n == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        l, r = 0, n - 1
        while l < n and r > 0 and l < r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                left, right = nums[l:m], nums[m+1:r+1]
                if len(left) == 0:
                    first = m
                else:
                    first = l + bisect_left(left, target)
                if len(right) == 0:
                    last = m
                else:
                    last = m + bisect_right(right, target)
                return [first, last]
        if nums[r] == nums[l] == target:
            return [l, r]
        return [-1, -1]


if __name__ == "__main__":
    max_num, size = 15, 10
    nums = np.sort(np.random.choice(list(range(max_num)), size=size)).tolist()
    target = np.random.choice(nums)
    # nums, target = [0, 1, 1, 1, 6, 9, 9, 10, 12, 14], 0
    # nums, target = [1, 1, 4, 4, 5, 7, 7, 11, 11, 12], 4
    print(f"{nums}, {target}")
    print(Solution2().searchRange(nums, target))

