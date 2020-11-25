from typing import List
import numpy as np


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        me = [[0] * (n + 1) for _ in range((m + 1))]  # me means max_edge
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "0":
                    me[i][j] = 0
                else:
                    me[i][j] = min(me[i - 1][j - 1], me[i][j - 1], me[i - 1][j]) + int(
                        matrix[i - 1][j - 1] == "1"
                    )
        print(matrix)
        print(np.array(me))
        max_edge = max([c for row in me for c in row])
        return max_edge * max_edge


if __name__ == "__main__":
    # assert (
    #     Solution().maximalSquare(
    #         [
    #             ["1", "0", "1", "0", "0"],
    #             ["1", "0", "1", "1", "1"],
    #             ["1", "1", "1", "1", "1"],
    #             ["1", "0", "0", "1", "0"],
    #         ]
    #     )
    #     == 4
    # )
    print(Solution().maximalSquare(np.random.choice([0, 1], size=25, p=[0.2, 0.8]).reshape(5, 5).astype(str)))
