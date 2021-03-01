from common import *


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """traverse in following the order: right --> middle --> left, 时间复杂度O(n)
        注：可以使用Morris遍历来将空间复杂度降为O(1), 主要是利用了树中的空闲指针.
        """
        if root is not None:
            self.visit(root, 0)
        return root

    def visit(self, root, cumsum):
        if root is None:
            return cumsum
        root.val += self.visit(root.right, cumsum)
        return self.visit(root.left, root.val)


if __name__ == "__main__":
    root = create_binary_tree([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
    logger.info(Solution().convertBST(root))
