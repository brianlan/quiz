from typing import List
from collections import defaultdict, Counter, deque
from itertools import accumulate
import time
import numpy as np
from loguru import logger
from math import inf, log2, floor


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def create_linked_list(nums: List) -> ListNode:
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    p = head
    for num in nums[1:]:
        p.next = ListNode(num)
        p = p.next
    return head


def linked_list_to_nums(head) -> List:
    nums = []
    p = head
    while p is not None:
        nums.append(p.val)
        p = p.next
    return nums


def create_binary_tree(nums: List) -> TreeNode:
    tot = len(nums)
    if tot == 0:
        return None
    # depth = floor(log2(tot)) + 1
    nodes = [None if num is None else TreeNode(num) for num in nums]
    for n in range(tot):
        if nodes[n] is None:
            continue
        d = floor(log2(n + 1))  # depth id
        j = n + 1 - 2 ** d  # pos id in i-th layer
        right_id = 2 ** (d + 1) + 2 * j
        left_id = right_id - 1
        try:
            nodes[n].right = nodes[right_id]
        except IndexError:
            pass
        try:
            nodes[n].left = nodes[left_id]
        except IndexError:
            pass
    return nodes[0]


def binary_tree_to_nums(root: TreeNode) -> List:
    pass
