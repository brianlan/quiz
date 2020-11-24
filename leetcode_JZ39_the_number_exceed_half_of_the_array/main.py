from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        the_number = None
        cnt = 0
        for i in range(len(nums)):
            if cnt == 0:
                the_number = nums[i]
                cnt = 1
                continue
            if the_number == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        return the_number
