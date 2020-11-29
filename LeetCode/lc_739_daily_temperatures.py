from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if len(T) == 0:
            return []
        stack = [0]  # stores index (position)
        ans = [0] * len(T)
        for i in range(1, len(T)):
            while stack and T[i] > T[stack[-1]]:
                pos = stack.pop()
                ans[pos] = i - pos
            stack.append(i)
        return ans


if __name__ == "__main__":
    assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
