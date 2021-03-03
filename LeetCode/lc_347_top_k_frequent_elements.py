from common import *
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        logger.debug(f"\n{nums}\n{k}")
        counter = defaultdict(int)
        _ = [counter.update({num: counter[num] + 1}) for num in nums]
        pq = []
        for num, cnt in counter.items():
            if len(pq) < k:
                heapq.heappush(pq, (cnt, num))
            else:
                if cnt >= pq[0][0]:  # peak the top of the heap
                    heapq.heapreplace(pq, (cnt, num))
        return [num for cnt, num in pq]


if __name__ == '__main__':
    # nums, k = [6, 4, 6, 3, 3, 6, 2, 1, 3, 5], 2
    # nums, k = [3, 4, 4, 3, 5, 4, 1, 6, 2, 1], 3
    nums, k = [1], 1
    # nums, k = (np.random.randint(6, size=10) + 1).tolist(), np.random.randint(6) + 1
    logger.info(Solution().topKFrequent(nums, k))
