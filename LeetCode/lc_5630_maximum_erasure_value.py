from common import *


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_score = 0
        i = 0
        cumsum = nums[0]
        idx_of_prev = {nums[0]: 0}
        for j in range(1, len(nums)):
            if nums[j] in idx_of_prev:  # duplicate value found
                max_score = max(max_score, cumsum)
                prev_j = idx_of_prev[nums[j]]
                for k in nums[i: prev_j + 1]:
                    del idx_of_prev[k]
                    cumsum -= k
                i = prev_j + 1
            cumsum += nums[j]
            idx_of_prev[nums[j]] = j
            j += 1
        return max(max_score, cumsum)


if __name__ == "__main__":
    nums = (np.random.randint(15, size=20) + 1).tolist()
    # nums = [4,2,4,5,6]
    # nums = [7, 6, 5, 8, 7, 1, 3, 3, 3, 8]
    # nums = [1, 4, 6, 1, 2, 5, 4, 10, 8, 3]
    # nums = list(range(10000)) * 10
    logger.debug(nums)
    logger.info(Solution().maximumUniqueSubarray(nums))
