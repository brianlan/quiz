from typing import List, Tuple
import copy
from loguru import logger
import numpy as np


class Solution:
    all_possibilities = {str(i + 1) for i in range(9)}

    def __init__(self):
        self.positions = []
        self.final_solution = None

    def get_values_in_9grid(self, board: List[List[str]], i, j) -> List[List[str]]:
        zi, zj = i // 3, j // 3
        return {
            x
            for row in board[3 * zi : 3 * (zi + 1)]
            for x in row[3 * zj : 3 * (zj + 1)]
        }

    def get_possibilities(self, board: List[List[str]], i, j) -> List[str]:
        return (
            self.all_possibilities
            - set(board[i])  # row-wise
            - set([x[j] for x in board])  # column-wise
            - self.get_values_in_9grid(board, i, j)  # in the same 9-grid
        )
    
    def done(self, board: List[List[str]]) -> bool:
        return all([x != '.' for row in board for x in row])

    def _try(self, board: List[List[str]], pos: int) -> None:
        while pos < len(self.positions):
            i, j = self.positions[pos]
            possibilities = self.get_possibilities(board, i, j)
            if not possibilities:
                return
            
            for p in possibilities:
                board[i][j] = p
                self._try(board, pos + 1)

            if self.done(board) and self.final_solution is None:
                self.final_solution = copy.deepcopy(board)

            board[i][j] = '.'

            return

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.positions = [
            (i, j)
            for i, row in enumerate(board)
            for j, cell in enumerate(row)
            if cell == "."
        ]
        self._try(board, 0)

        logger.debug(f"\n{np.array(self.final_solution)}")

        for i in range(9):
            for j in range(9):
                board[i][j] = self.final_solution[i][j]
        


if __name__ == "__main__":
    Solution().solveSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
