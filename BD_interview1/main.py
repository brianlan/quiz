class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class MaxDepthLessThanKError(Exception):
    pass


def find_num_nodes_at_depth(root, k):
    if root is None:
        return 0
    queue = [root]
    depth = 0
    while len(queue) > 0:
        cnt = len(queue)
        if depth == k:
            return cnt
        depth += 1
        new_queue = []
        for i in queue:
            if i.left is not None:
                new_queue.append(i.left)
            if i.right is not None:
                new_queue.append(i.right)
        queue = new_queue
    raise MaxDepthLessThanKError(f"Exceeds max depth of tree, the depth is {depth}")



