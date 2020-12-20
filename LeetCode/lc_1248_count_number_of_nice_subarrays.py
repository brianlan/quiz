from common import *


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] + [-1] * n  # pre[i] stores number of odd numbers as of i, pre[0] === 0, as it means the subarray is []
        cnt = [1] + [0] * (n)  # cnt[i] stores frequency of each pre[i] values as of i. cnt[0] initialized as 1
        num_nice_subarrays = 0
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + int(nums[i - 1] % 2 == 1)
            cnt[pre[i]] += 1
            num_nice_subarrays += cnt[pre[i] - k]
        logger.debug(pre)
        logger.debug(cnt)
        return num_nice_subarrays


if __name__ == "__main__":
    # nums, k = [18,15,20,20,5,11,13,15,15,11], 2
    # nums, k = [1,1,2,1,1], 3
    # nums, k = [2,4,6], 1
    # nums, k = [2,2,2,1,2,2,1,2,2,2], 2
    nums, k = [1,1,1,1,1], 1
    # nums, k = (np.random.randint(20, size=10) + 1).tolist(), np.random.randint(10) + 1
    logger.debug(nums)
    logger.debug(k)
    print(Solution().numberOfSubarrays(nums, k))