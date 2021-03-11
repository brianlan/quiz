from common import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        logger.debug(f"\n{nums}")
        n = len(nums)
        dp = [-inf for i in range(n + 1)]
        for i in range(1, n + 1):
            dp[i] = max(nums[i - 1], dp[i - 1] + nums[i - 1])
        return max(dp)

if __name__ == '__main__':
    nums = (np.random.randint(21, size=100) - 10).tolist()
    logger.info(Solution().maxSubArray(nums))
