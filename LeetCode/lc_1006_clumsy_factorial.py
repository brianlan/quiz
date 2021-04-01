from common import *
from itertools import cycle


class Solution:
    def gen_expression(self, N: int) -> str:
        ops = cycle(["*", "//", "+", "-"])
        parts = [str(N)]
        for n in range(N - 1, 0, -1):
            op = next(ops)
            parts.append(op)
            parts.append(str(n))
        return "".join(parts)

    def clumsy(self, N: int) -> int:
        logger.debug(f"{N=}")
        if N == 1:
            return 1
        expression = self.gen_expression(N)
        logger.debug(expression)
        return eval(expression)


if __name__ == '__main__':
    # N = np.random.randint(21) + 1
    N = 11
    logger.info(Solution().clumsy(N))
