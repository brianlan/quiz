from typing import List
from collections import defaultdict, Counter, deque
from itertools import accumulate
import time
import numpy as np
from loguru import logger
from math import inf


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def measure(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        res = func(*args, **kwargs)
        logger.info(f"function {func.__name__} spent: {(time.time() - t0) * 1000:.2} ms")
        return res
    return wrapper


def create_linked_list(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    p = head
    for num in nums[1:]:
        p.next = ListNode(num)
        p = p.next
    return head


def linked_list_to_nums(head):
    nums = []
    p = head
    while p is not None:
        nums.append(p.val)
        p = p.next
    return nums
