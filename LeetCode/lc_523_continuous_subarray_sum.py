from common import *


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """We must consider the case where n equals 0 in this quiz
        """
        logger.debug(f"\n{nums}, {k}")
        tot = len(nums)
        if tot < 2:
            return False

        # if there're 2 or more consecutive 0 in nums, the result is always True with n = 0
        for i in range(tot - 1):
            if nums[i] == 0 and nums[i + 1] == 0:
                return True

        if k == 0:  # if no more than 2 consecutive 0, k can't be 0
            return False

        k = abs(k)  # can always turn k into positive number by choosing n to be a negative integer

        cache = {0: -1}
        running_sum = 0
        for i in range(tot):
            running_sum += nums[i]
            residual = running_sum % k
            if (residual in cache) and (i - cache[residual] >= 2):
                # logger.debug(f"\n{i=}, {running_sum=} {cache=}")
                return True
            cache[residual] = cache.get(residual, i)
        # logger.debug(f"\n{cache}")
        return False


if __name__ == "__main__":
    # nums, k = [1, 4, 5, 2, 3, 1, 3, 1], 5
    # nums, k = [23, 2, 4, 6, 7], 6  # presum array: [23, 25, 29, 35, 42]
    # nums, k = [23, 2, 6, 4, 7], 6
    # nums, k = [9, 17, 5, 11, 10, 13, 12, 15, 19, 18, 16, 18], 1
    # nums, k = [23,2,0,6,7], 0
    # nums, k = [0, 0], -1
    # nums, k = [23, 2, 6, 4, 7], -6
    # nums, k = [1, 1], -1
    # nums, k = [1, 0], 2
    # nums, k = [1, 2, 12], 6
    nums, k = (np.random.randint(50000, size=500)).tolist(), np.random.randint(1000000) - 500000
    logger.info(Solution().checkSubarraySum(nums, k))
