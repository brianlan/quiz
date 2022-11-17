import math
from typing import Optional

import numpy as np
from loguru import logger

from common import create_binary_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_text = Solution.inorder(root, None)
        subroot_text = Solution.inorder(subRoot, None)
        if root_text.find(subroot_text) == -1:
            return False
        else:
            return True

    @staticmethod
    def inorder(root, src) -> str:
        if root is None:
            return src
        return Solution.inorder(root.left, "L") + str(root.val) + Solution.inorder(root.right, "R")


if __name__ == '__main__':
    assert Solution().isSubtree(create_binary_tree([3,4,5,1,2]), create_binary_tree([4, 1, 2])) is True
    assert Solution().isSubtree(create_binary_tree([3,4,5,1,2,None,None,None,None,0]), create_binary_tree([4, 1, 2])) is False
    assert Solution().isSubtree(create_binary_tree([4,1,None,None,2]), create_binary_tree([1,None,4,2])) is False
