from typing import List
import numpy as np
from numpy.core.defchararray import replace


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 9999999
        if n == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        mid = n // 2 - 1
        return min(self.findMin(nums[:mid]), nums[mid], self.findMin(nums[mid+1:]))


if __name__ == "__main__":
    max_num, size = 20, 10
    nums = np.sort(np.random.choice(list(range(max_num)), size=size, replace=False)).tolist()
    cut = np.random.randint(10)
    nums = nums[cut:] + nums[:cut]
    # nums = [3, 4, 6, 10, 11, 15, 16, 17, 0, 2]
    print(nums)
    print(Solution().findMin(nums))
