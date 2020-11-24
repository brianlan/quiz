from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        opt = [[None] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            opt[i][0] = 0
        for j in range(n + 1):
            opt[0][j] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                opt[i][j] = grid[i - 1][j - 1] + max(opt[i - 1][j], opt[i][j - 1])
        return opt[m][n]


if __name__ == "__main__":
    print(
        Solution().maxValue(
            [
                [3, 1, 5, 16, 7],
                [16, 8, 4, 2, 3],
                [1, 6, 9, 18, 7],
                [1, 4, 7, 27, 5],
                [2, 3, 15, 6, 8],
            ]
        )
    )
