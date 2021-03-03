from common import *


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        logger.debug(f"\n{np.array(matrix)}")
        nrows = len(matrix)
        ncols = 0 if nrows == 0 else len(matrix[0])
        self.cumsum_2d = []
        if nrows > 0 and ncols > 0:
            self.cumsum_2d = [[0] * (ncols + 1) for i in range(nrows + 1)]
            for i in range(1, nrows + 1):
                for j in range(1, ncols + 1):
                    self.cumsum_2d[i][j] = (
                        self.cumsum_2d[i - 1][j]
                        + self.cumsum_2d[i][j - 1]
                        - self.cumsum_2d[i - 1][j - 1]
                        + matrix[i - 1][j - 1]
                    )
        logger.debug(f"\n{np.array(self.cumsum_2d)}")

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.cumsum_2d:
            return (
                self.cumsum_2d[row2 + 1][col2 + 1]
                - self.cumsum_2d[row1][col2 + 1]
                - self.cumsum_2d[row2 + 1][col1]
                + self.cumsum_2d[row1][col1]
            )
        return 0


if __name__ == "__main__":
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    logger.info(NumMatrix(matrix).sumRegion(2, 1, 4, 3))
