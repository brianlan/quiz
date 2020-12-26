from typing import List
from collections import defaultdict, Counter, deque
from itertools import accumulate
import time
import numpy as np
from loguru import logger


def measure(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        res = func(*args, **kwargs)
        logger.info(f"function {func.__name__} spent: {(time.time() - t0) * 1000:.2} ms")
        return res
    return wrapper
