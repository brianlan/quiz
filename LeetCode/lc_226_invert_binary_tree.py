from common import *

class Solution:
    def invert(self, root: TreeNode) -> None:
        if root.left is not None:
            self.invert(root.left)
        if root.right is not None:
            self.invert(root.right)
        root.left, root.right = root.right, root.left

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        self.invert(root)
        return root

if __name__ == '__main__':
    root = create_binary_tree(
        [10,5,17,3,8,None,24,None,4,7,9,None,None,20,None,None,None,None,None,None,None,None,None,None,None,None,None,19,22,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,18]
    )
    logger.info(Solution().invertTree(root))
    pass