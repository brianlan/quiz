from typing import List
from loguru import logger
import json


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pass


def gen_problem(settings):
    return [str(k) for k, v in settings.items() for _ in range(v)]


if __name__ == "__main__":
    logger.info(json.dumps(gen_problem({"A": 5, "B": 6, "C": 1, "D": 1, "E": 4, "F": 3})))
    logger.info(json.dumps(gen_problem({"A": 5, "B": 6, "C": 3, "D": 1, "E": 4, "F": 4})))
    logger.info(Solution().leastInterval())
