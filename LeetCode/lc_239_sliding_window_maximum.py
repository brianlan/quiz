from common import *
from data_structures.queue import MinMaxQueue

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        k = min(k, n)
        window = MinMaxQueue(nums[:k], type="max")
        ans = []
        ans.append(window.max())
        for i in range(n - k):
            window.dequeue()
            window.enqueue(nums[i+k])
            ans.append(window.max())
        return ans


if __name__ == "__main__":
    # nums, k = (np.random.randint(20000, size=100000) - 10000).tolist(), np.random.randint(100000) + 1
    nums, k = [-7,-8,7,5,7,1,6,0], 4
    logger.debug(nums)
    logger.debug(k)
    logger.info(Solution().maxSlidingWindow(nums, k))
