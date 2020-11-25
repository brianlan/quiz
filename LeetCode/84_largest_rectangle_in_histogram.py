from typing import List
import numpy as np

class Solution:
    @profile
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0
        max_area = -1
        for i in range(n):
            min_val = heights[i]
            for j in range(i, n):
                min_val = min(heights[j], min_val)
                max_area = max(max_area, (j - i + 1) * min_val)
        # print(heights)
        return max_area


if __name__ == "__main__":
    print(Solution().largestRectangleArea(list(range(1, 10000))))
    # print(Solution().largestRectangleArea([6]))
    # print(Solution().largestRectangleArea(np.random.randint(10, size=10) + 1))