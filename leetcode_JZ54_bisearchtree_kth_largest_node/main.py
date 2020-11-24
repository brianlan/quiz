from typing import Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class KthFound(Exception):
    def __init__(self, kth) -> None:
        self.kth = kth


class Solution:
    def find(self, root: TreeNode, k: int) -> Tuple[int, int]:
        if root is None:
            return None, 0
        # kth, left_tot = self.find(root.left, k)
        kth, right_tot = self.find(root.right, k)
        if kth is not None:
            raise KthFound(kth)
        if right_tot == k - 1:
            raise KthFound(root.val)
        kth, left_tot = self.find(root.left, k - right_tot - 1)
        return kth, left_tot + right_tot + 1
        
    def kthLargest(self, root: TreeNode, k: int) -> int:
        try:
            self.find(root, k)
        except KthFound as e:
            return e.kth


class Solution2:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # 右根左 非递归遍历 
        stack,p,count = [],root,0
        while p or stack:
            while p:
                stack.append(p)
                p = p.right
            if stack:
                curr = stack.pop()
                count += 1
                if count == k:return curr.val
                p = curr.left


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print(Solution().kthLargest(root, 4))