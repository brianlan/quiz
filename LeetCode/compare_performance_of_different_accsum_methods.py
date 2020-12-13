import time
from functools import reduce
from itertools import accumulate
from loguru import logger
import numpy as np


def measure(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        res = func(*args, **kwargs)
        logger.info(f"function {func.__name__} spent: {(time.time() - t0) * 1000:.2} ms")
        return res
    return wrapper


@measure
def forloop(nums):
    n = len(nums)
    accsum = [0] * (n+1)
    for i in range(1,n+1):
        accsum[i] = nums[i-1] + accsum[i-1]
    return accsum[1:]


@measure
def use_reduce(nums):
    """
    in the lambda function, x is 2-element tuple, the first one is a list,
    storing the cumulative sum at each position, while the second one 
    is the latest sum-over value as of now.
    """
    return reduce(lambda x, y: (x[0] + [y+x[1]], y+x[1]), nums, ([], 0))[0]


@measure
def numpy_cumsum(nums):
    return np.cumsum(nums).tolist()


@measure
def functools_accumulate(nums):
    return list(accumulate(nums))


def accsum_generator(nums):
    total = 0
    for i in nums:
        total += i
        yield total


@measure
def generator(nums):
    return list(accsum_generator(nums))


if __name__ == "__main__":
    players = [forloop, use_reduce, numpy_cumsum, functools_accumulate, generator]
    nums = np.random.randint(100, size=10000).tolist()
    gt = np.cumsum(nums).tolist()
    for func in players:
        accsum = func(nums)
        assert accsum == gt, f"{accsum} != {gt}"
