from common import *

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def create_random_linked_list(nums):
    n = len(nums)
    if n == 0:
        return None
    nodes = [Node(num[0]) for num in nums]
    for i, num in enumerate(nums):
        if i < len(nums) - 1:
            nodes[i].next = nodes[i + 1]
        nodes[i].random = None if num[1] is None else nodes[num[1]]
    return nodes[0]


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        p = head
        prev = new_head = None
        cache = {}
        while p is not None:
            if id(p) in cache:
                node = cache[id(p)]
            else:
                node = Node(p.val)
                cache[id(p)] = node
            if p is head:  # first node
                prev = new_head = node
            else:
                prev.next = node
                prev = node
            if p.random is not None:
                if id(p.random) not in cache:
                    cache[id(p.random)] = Node(p.random.val)
                node.random = cache[id(p.random)]
            p = p.next
                
        return new_head


if __name__ == '__main__':
    # head = create_random_linked_list([[7,None],[13,0],[11,4],[10,2],[1,0]])
    head = create_random_linked_list([[8, 0]])
    logger.info(linked_list_to_nums(Solution().copyRandomList(head)))
