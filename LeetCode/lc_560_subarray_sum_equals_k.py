from typing import List
from loguru import logger
import numpy as np
from itertools import accumulate
from collections import defaultdict


class Solution:
    """Brutal force double forloop => O(n^2)"""
    def subarraySum(self, nums: List[int], k: int) -> int:
        logger.debug(f"{nums=}, {k=}")
        n = len(nums)
        s = [[0] * n for _ in range(n)]
        n_meet = 0
        for i in range(n):
            s[i][i] = nums[i]
            if s[i][i] == k:
                n_meet += 1
        for i in range(n - 1):
            for j in range(i + 1, n):
                s[i][j] = s[i][j - 1] + nums[j]
                if s[i][j] == k:
                    n_meet += 1
        logger.debug(f"\n{np.array(s)}")
        return n_meet


class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        presum = [0] + list(accumulate(nums))
        logger.debug(presum)
        # s = [[0] * n for _ in range(n)]
        n_meet = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if presum[j] - presum[i] == k:
                    n_meet += 1
        # logger.debug(f"\n{np.array(s)}")
        return n_meet


class Solution3:
    def subarraySum(self, nums: List[int], k: int) -> int:
        logger.debug(f"{nums=}, {k=}")
        pre_sum_freq = defaultdict(int)
        pre_sum_freq[0] = 1
        presum = 0
        n_meet = 0
        for num in nums:
            presum += num

            # 1. 这里的含意是看 presum[cur] - presum[prev] == k是否存在
            #    该公式进行调整之后变为看 presum[cur] - k 是否在之前的presum中(presum[prev])出现过
            #    而整个题目就等价于看有几种cur和prev的组合（或者说i和j的组合）满足presum[cur] - presum[prev] == k
            # 2. 一般我们计算这种双变量的组合都是双重循环，复杂度为O(n^2)，
            #    但这个解法的巧妙之处就在于: 用查某个key是不是在dict中，从而减少了一个循环层次，
            # 3. 相当于还是检查了当前presum[cur]的情况下, 之前所有的presum[prev]中
            #    是否有满足条件的：pre_sum_freq把之前出现过的每个位置的presum值都用dict的方式存下来了。
            #    因此，如果不用dict存，那么我们就需要去遍历之前每个位置i的presum值来看是否满足presum[cur] - presum[i] == k
            if presum - k in pre_sum_freq:
                n_meet += pre_sum_freq[presum - k]  # 我们用dict来存储之前所有的presum[prev]出现的次数, 因此n_meet就可以加等这么多次
            
            pre_sum_freq[presum] += 1
        return n_meet


if __name__ == "__main__":
    # nums, k = [1, 4, 5, 2, 3, 1, 3, 1], 5
    nums, k = [-4, -3,  4,  5, -2, -9, -8,  6], 4
    # nums, k = np.random.randint(20, size=8) - 10, np.random.randint(20) - 10
    logger.info(Solution3().subarraySum(nums, k))
