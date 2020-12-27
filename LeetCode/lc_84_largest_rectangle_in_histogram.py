from typing import List
import numpy as np


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """brutal force, double for loop to calculate every possible range."""
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
        """brutal force, for each bar search it's left and right."""
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


class Solution3:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """mono-stack"""
        if len(heights) == 1 and heights[0] == 0:
            return 0
        heights = [0] + heights + [0]  # sentinel
        n = len(heights)
        if n == 2:
            return 0
        max_area = 0
        stack = [0]  # stack stores index (position) rather than height value.
        for i in range(1, n):
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1  # stack[-1] is the new top of stack
                max_area = max(max_area, cur_height * cur_width)
            stack.append(i)
        return max_area


if __name__ == "__main__":
    import time

    t0 = time.time()
    # heights = list(range(1, 10000))
    # heights = np.random.randint(10, size=10) + 1
    heights = [5, 7, 5, 8, 3, 2, 10, 2, 7, 8]
    # print(Solution().largestRectangleArea([6]))
    print(heights)
    print(Solution3().largestRectangleArea(heights))
    print(f"elapsed time: {time.time() - t0:.2f}")
