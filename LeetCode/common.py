from typing import List, Tuple
from collections import defaultdict, Counter, deque
import heapq
from itertools import accumulate
from functools import lru_cache
import bisect
import time
import numpy as np
from loguru import logger
from math import inf, log2, floor
from dataclasses import dataclass, field
from typing import Any
import copy


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f'{self.val}'


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
    # prev_layer = nodes[:1]
    j, k = 0, 1
    while k < tot:
        # num_prev_effective_nodes = sum([n is not None for n in prev_layer])
        # num_prev_effective_nodes = sum([n is not None for n in nodes[i:k]])
        # prev_layer_size = k - i
        # while k < min(prev_layer_size * 2, tot):
        # for j in range(len(prev_layer)):
        if nodes[j] is None:
            j += 1
            continue
        else:
        # if prev_layer[j] is not None:
            try:
                nodes[j].left = nodes[k]
                k += 1
            except IndexError:
                nodes[j].left = None
            
            try:
                nodes[j].right = nodes[k]
                k += 1
            except IndexError:
                nodes[j].right = None
        j += 1

        # prev_layer = nodes[i:i+num_prev_effective_nodes * 2]
        # i = j = j + 1
    return nodes[0]


def binary_tree_to_nums(root: TreeNode) -> List:
    pass
