import math
from typing import List

import numpy as np
from loguru import logger


class Solution:
    def __init__(self) -> None:
        self.critical_points = None

    def numDistinct(self, s: str, t: str) -> int:
        ns, nt = len(s), len(t)
        if ns < nt:
            return 0
        self.critical_points = [[] for _ in range(nt)]
        dp = [[None] * (nt + 1) for _ in range(ns + 1)]

        for i in range(ns + 1):
            dp[i][0] = 0

        for i in range(nt + 1):
            dp[0][i] = 0

        for j in range(1, nt + 1):
            for i in range(1, ns + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if i >= j:
                        self.critical_points[j - 1].append(i - 1)
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        
        if dp[-1][-1] == nt:
            solutions = []
            num_solutions = self.calc_num_solutions(solutions, [])
            return num_solutions

        return 0

    def calc_num_solutions(self, solutions, path):
        current_pos = len(path)
        if current_pos == len(self.critical_points):
            solutions.append(path)
            return
        for i in range(len(self.critical_points[current_pos]) - 1, -1, -1):  # 反过来遍历，配合不满足要求时break，可以稍微减少一些计算量
            pt = [self.critical_points[current_pos][i]]
            if not path:
                self.calc_num_solutions(solutions, path + [pt])
            else:
                if path[-1] < pt:
                    self.calc_num_solutions(solutions, path + [pt])
                else:
                    break

        return len(solutions)


if __name__ == '__main__':
    assert Solution().numDistinct("rabbbit", "rabbit") == 3
    assert Solution().numDistinct("babgbag", "bag") == 5
    assert Solution().numDistinct("laryylrry", "lry") == 7
    assert Solution().numDistinct(
        "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe",
        "bddabdcae"
    ) == 10582116
