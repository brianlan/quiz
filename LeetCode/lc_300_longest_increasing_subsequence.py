import math
from typing import List

import numpy as np
from loguru import logger


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))
        for i in range(1, len(nums)):
            compare_result = [dp[j] + 1 for j in range(i) if nums[i] > nums[j]]
            if compare_result:
                dp[i] = max(compare_result)
        # logger.debug(dp)
        # logger.debug(nums)
        return max(dp)


if __name__ == "__main__":
    assert Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
    assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
    assert Solution().lengthOfLIS([1, 3, 6, 5, 2, 1, 2, 0, 2, 4, 6, 9, 2, 0, 5, 19, 11, 12, 13]) == 8