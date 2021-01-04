from common import *
from collections import deque


class Solution:
    """
    Pure DP, will get Time Exceeded due to max(0, i-k) 
    when n and k are both large
    """
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [None] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[max(0, i-k):i]) + nums[i]
        return dp[-1]


class Solution1:
    """
    Eliminated max(0, i-k), and use minimum queue to get the max
    value in the moving sliding window. 
    """
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [None] * n
        dp[0] = nums[0]
        helper = deque()
        helper.append(dp[0])
        for i in range(1, n):
            dp[i] = helper[0] + nums[i]
            if i >= k and dp[i-k] == helper[0]:
                helper.popleft()
            try:
                while dp[i] > helper[-1]:
                    helper.pop()
            except IndexError:
                pass
            helper.append(dp[i])
                
        return dp[-1]


if __name__ == "__main__":
    # nums, k = [1,-1,-2,4,-7,3], 2
    # nums, k = [10,-5,-2,4,0,3], 3
    nums, k = [1,-5,-20,4,-1,3,-6,-3], 2
    logger.info(Solution1().maxResult(nums, k))
