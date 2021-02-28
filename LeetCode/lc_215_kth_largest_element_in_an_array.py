from common import *
import heapq


class Solution:
    """分治思想，类似于快排的方式
    注意点：每次都在partition中随机选择一个位置作为参考值，而不是固定某个位置
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pass


class Solution2:
    """用大小为K的优先队列来处理
    优先队列的具体实现方式可以直接选用堆，
    至于是最大堆还是最小堆，可以看k跟0靠的近，还是跟len(nums)靠的近
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        logger.debug(f"\n{nums}\n{k}")
        n = len(nums)
        priority_queue = nums[:k]
        heapq.heapify(priority_queue)
        for i in range(k, n):
            if nums[i] > priority_queue[0]:
                heapq.heapreplace(priority_queue, nums[i])
        return priority_queue[0]


if __name__ == "__main__":
    # nums, k = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
    # nums, k = [3,2,1,5,6,4], 2
    nums, k = np.random.randint(10, size=20).tolist(), np.random.randint(20) + 1
    logger.info(Solution2().findKthLargest(nums, k))
