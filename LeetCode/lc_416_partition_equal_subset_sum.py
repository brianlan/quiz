from common import *
from math import inf

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """建模成01背包问题
        背包容量(C):   sum(nums) / 2
        物品cost:     nums[i]
        物品value:    nums[i]
        这样建模相当于是选取数字只和尽可能大于或等于C, 由于C是背包容量限制，所以最佳情况
        就是所有数字加起来正好等于C
        """
        n = len(nums)
        tot = sum(nums)
        logger.debug(f"{nums=}, {n=}, {tot=}")
        if n < 2:
            return False
        if tot % 2 != 0:
            return False
        capacity = tot // 2
        dp = [[-inf] * (capacity + 1) for i in range(n)]

        # initialization
        for i in range(n):
            dp[i][0] = 0
        # for j in range(1, capacity + 1):
        #     dp[0][j] = 0 if nums[0] > j else nums[0]

        # dp
        for i in range(1, n):
            cost = value = nums[i]
            for j in range(capacity + 1):
                if cost > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + value)
        logger.debug(f"\n{np.array(dp)}")
        return dp[-1][-1] == capacity


if __name__ == "__main__":
    # nums = [1, 5, 11, 5]
    # nums = [1, 2, 3, 5]
    # nums = [15, 8, 6, 6, 3, 10, 13, 13, 5, 19]
    # nums = [2,2,3,5]
    # nums = [92, 39, 83, 11, 66, 80, 51, 96, 11, 41, 29, 2, 88, 22, 23, 33, 70, 79, 25, 82, 84, 42, 46, 81, 36, 29, 16, 26, 45, 35, 95, 4, 3, 48, 10, 58, 16, 9, 80, 67, 20, 80, 76, 15, 80, 36, 24, 100, 66, 5, 82, 41, 90, 57, 23, 83, 15, 90, 52, 49, 11, 78, 97, 65, 54, 56, 64, 7, 52, 62, 2, 59, 24, 98, 71, 93, 44, 78, 5, 37, 44, 76, 95, 74, 20, 98, 87, 46, 83, 42, 4, 86, 23, 74, 84, 71, 86, 69, 59, 76, 84, 63, 31, 82, 78, 22, 43, 19, 73, 29, 20, 77, 74, 60, 99, 100, 83, 66, 71, 51, 6, 62, 87, 60, 55, 63, 53, 42, 95, 40, 39, 98, 18, 44, 93, 74, 29, 1, 73, 84, 2, 92, 28, 63, 14, 100, 32, 67, 10, 67, 8, 100, 48, 20, 41, 10, 17, 89, 26, 68, 4, 6, 93, 5, 44, 1, 97, 85, 11, 3, 40, 31, 1, 17, 65, 15, 34, 99, 1, 49, 39, 19, 28, 69, 41, 24, 25, 14, 14, 75, 44, 10, 76, 49, 33, 25, 37, 36, 18, 51]
    nums = (np.random.randint(100, size=10) + 1).tolist()
    # while True:
    #     nums = (np.random.randint(100, size=10) + 1).tolist()
    #     if sum(nums) % 2 == 0:
    #         break
    logger.info(nums)
    logger.info(Solution().canPartition(nums))
