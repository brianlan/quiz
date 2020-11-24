from typing import List


class Solution:
    """Bruital force"""
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = -1
        for i in range(n - 1):
            for j in range(i + 1, n):
                min_edge = min(height[i], height[j])
                area = min_edge * (j - i)
                if area > max_area:
                    max_area = area
        return max_area


class Solution2:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = -1
        for r in range(1, n):  # r: right
            stop = False
            for l in range(0, r):  # l: left
                if height[l] < height[r]:
                    area = height[l] * (r - l)
                else:
                    area = height[r] * (r - l)
                    stop = True
                if area > max_area:
                    max_area = area
                if stop:
                    break
            
        return max_area


class Solution3:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = -1
        while l != r:
            area = min(height[r], height[l]) * (r - l)
            if area > max_area:
                max_area = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

if __name__ == "__main__":
    print(Solution3().maxArea([1,2,4,5,2,1,5,2,3,1,1,1,1,1,1,1,1,1,1,1]))
