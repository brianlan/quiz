from heapq import heappush, heappop

class Solution:
    init_ugly_nums = [2, 3, 5]

    def nthUglyNumber(self, n: int) -> int:
        heap, ugly_nums = [1], []
        while len(ugly_nums) < n:
            pop = heappop(heap)
            ugly_nums.append(pop)
            while heap and heap[0] == pop:  # remove duplicated value in the heap like 6=2x3=3x2
                heappop(heap)
            for u in self.init_ugly_nums:
                heappush(heap, u * pop)
        return ugly_nums[n - 1]


if __name__ == "__main__":
    print(Solution().nthUglyNumber(10))
    print(Solution().nthUglyNumber(1690))
