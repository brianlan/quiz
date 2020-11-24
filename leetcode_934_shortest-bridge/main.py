from typing import List


class Solution:
    def find_first_island(self, i, j, A):
        self.visit(i + 1, j, A)
        self.visit(i, j + 1, A)
        self.visit(i - 1, j, A)
        self.visit(i, j - 1, A)

    def visit(self, i, j, A):
        if i >= len(A) or i < 0 or j >= len(A[0]) or j < 0:
            return
        if self.first_island[i][j] != -1:
            return
        self.first_island[i][j] = A[i][j]
        if A[i][j] == 1:
            self.find_first_island(i, j, A)

    def find_first_1(self, A):
        for i, row in enumerate(A):
            for j, c in enumerate(row):
                if c == 1:
                    self.first_island[i][j] = 1
                    return i, j

    def build_bridge(self, first_island_points, A):
        expand_zone = first_island_points
        visited = set()
        steps = 0
        while len(expand_zone) > 0:
            new_expand_zone = set()
            for i, j in expand_zone:
                if A[i][j] == 1 and self.first_island[i][j] != 1:
                    return steps - 1
                if (
                    i + 1 < len(A)
                    and self.first_island[i + 1][j] != 1
                    and (i + 1, j) not in visited
                ):
                    new_expand_zone |= {(i + 1, j)}
                if (
                    i - 1 >= 0
                    and self.first_island[i - 1][j] != 1
                    and (i - 1, j) not in visited
                ):
                    new_expand_zone |= {(i - 1, j)}
                if (
                    j + 1 < len(A[0])
                    and self.first_island[i][j + 1] != 1
                    and (i, j + 1) not in visited
                ):
                    new_expand_zone |= {(i, j + 1)}
                if (
                    j - 1 >= 0
                    and self.first_island[i][j - 1] != 1
                    and (i, j - 1) not in visited
                ):
                    new_expand_zone |= {(i, j - 1)}
            expand_zone = new_expand_zone
            visited |= new_expand_zone
            print(expand_zone)
            steps += 1

    def shortestBridge(self, A: List[List[int]]) -> int:
        self.first_island = [[-1] * len(a) for a in A]  # -1 means not visited
        self.find_first_island(*self.find_first_1(A), A)
        print(self.first_island)
        steps = self.build_bridge(self.get_first_island_points(), A)
        return steps

    def get_first_island_points(self):
        island_points = []
        for i in range(len(self.first_island)):
            for j in range(len(self.first_island[i])):
                if self.first_island[i][j] == 1:
                    island_points.append((i, j))
        return island_points


if __name__ == "__main__":
    # A = [
    #     [1, 1, 1, 1, 1],
    #     [0, 0, 1, 0, 1],
    #     [0, 0, 1, 1, 1],
    #     [1, 1, 0, 0, 0],
    #     [0, 1, 0, 0, 0],
    # ]
    A = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 1],
    ]
    print(Solution().shortestBridge(A))
