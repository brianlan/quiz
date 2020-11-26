from typing import List
import numpy as np

class Solution:
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


class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0

        for i in range(size):
            left = i
            cur_height = heights[i]
            while left > 0 and heights[left - 1] >= cur_height:
                left -= 1

            right = i
            while right < size - 1 and heights[right + 1] >= cur_height:
                right += 1

            max_width = right - left + 1
            res = max(res, max_width * cur_height)
        return res


if __name__ == "__main__":
    import time
    t0 = time.time()
    print(Solution2().largestRectangleArea(list(range(1, 10000))))
    # print(Solution().largestRectangleArea([6]))
    # print(Solution().largestRectangleArea(np.random.randint(10, size=10) + 1))
    print(f"elapsed time: {time.time() - t0:.2f}")