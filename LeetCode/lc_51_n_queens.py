from collections import defaultdict
from common import *

class Solution:
    def __init__(self) -> None:
        self.solutions = set()
        self.masks = defaultdict(lambda: defaultdict(list))

    def build_masks(self, n: int) -> None:
        diag_offsets = [[(ofs, ofs), (ofs, -ofs), (-ofs, ofs), (-ofs, -ofs)] for ofs in range(1, n)]
        diag_offsets = [j for i in diag_offsets for j in i]  # flatten
        for i in range(n):
            for j in range(n):
                self.masks[i][j] = [[False] * n for _ in range(n)]
                self.masks[i][j][i] = [True] * n
                for c in range(n):
                    self.masks[i][j][c][j] = True
                for o in diag_offsets:
                    if (0 <= i+o[0] < n) and (0 <= j+o[1] < n):
                        self.masks[i][j][i+o[0]][j+o[1]] = True

    def translate_solution(self, solution) -> Tuple[str]:
        cvt = {True: 'Q', False: '.'}  # conversion
        return tuple(''.join([cvt[item] for item in row]) for row in solution)

    def dfs(self, queens: List[List[bool]], occupied: List[List[bool]], start: Tuple[int, int], num_queens_to_place: int) -> bool:
        if num_queens_to_place == 0:
            self.solutions.add(self.translate_solution(copy.deepcopy(queens)))
            return 
        if all([cell for row in occupied for cell in row]):
            return 
        n = len(queens)
        unoccupied = [(i, j) for i in range(n) for j in range(n) if not occupied[i][j] and i >= start[0] and j >= start[1]]
        for i, j in unoccupied:
            undo = []
            _mask = self.masks[i][j]
            for r in range(n):
                for c in range(n):
                    if not occupied[r][c] and _mask[r][c]:
                        occupied[r][c] = True
                        undo.append((r, c))
            queens[i][j] = True
            queens[i][j] = False
            for u in undo:
                occupied[u[0]][u[1]] = False

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.build_masks(n)
        queens = [[False] * n for _ in range(n)]
        occupied = [[False] * n for _ in range(n)]
        self.dfs(queens, occupied, n)
        return [list(s) for s in self.solutions]


class Solution2:
    def __init__(self) -> None:
        self.solutions = set()
        self.col = {}  # store collision status
        self.main_diag = {}  # store collision status
        self.sub_diag = {}  # store collision status

    def translate_solution(self, solution) -> Tuple[str]:
        n = len(solution)
        res = []
        for col in solution:
            res.append("." * col + "Q" + "." * (n - col - 1))
        return res

    def dfs(self, placed_queens: List[int], n: int) -> None:
        if len(placed_queens) == n:
            self.solutions.add(tuple(placed_queens))
            return 
        cur_row = len(placed_queens)
        for j in range(n):
            row_minus_col = cur_row - j
            row_add_col = j + cur_row
            if j not in self.col and row_minus_col not in self.main_diag and row_add_col not in self.sub_diag:
                self.col[j] = True
                self.main_diag[row_minus_col] = True
                self.sub_diag[row_add_col] = True
                self.dfs(placed_queens + [j], n)
                del self.col[j]
                del self.main_diag[row_minus_col]
                del self.sub_diag[row_add_col]

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.dfs([], n)
        return [self.translate_solution(s) for s in self.solutions]


if __name__ == '__main__':
    n = 6
    logger.info(Solution2().solveNQueens(n))
