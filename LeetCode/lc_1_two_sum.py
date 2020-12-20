from common import *


class Solution:
    @measure
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution2:
    @measure
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}  # key-value pair - num:idx
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev:
                return prev[diff], i
            prev[num] = i


if __name__ == "__main__":
    # nums, target = [2, 7, 11, 15], 9
    nums = np.random.choice(range(10000), size=1000, replace=False).tolist()
    target = nums[np.random.randint(1000)] + nums[np.random.randint(1000)]
    logger.info(target)
    
    i, j = Solution().twoSum(nums, target)
    logger.info(nums[i] + nums[j])

    i, j = Solution2().twoSum(nums, target)
    logger.info(nums[i] + nums[j])
