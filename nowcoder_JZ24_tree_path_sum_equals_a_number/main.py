# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.results = []

    @staticmethod
    def _is_leaf_node(node):
        return node.left is None and node.right is None

    def find(self, root, expectNumber, memo):
        if self._is_leaf_node(root):
            path = memo + [root.val]
            if sum(path) == expectNumber:
                self.results.append(path)
        else:
            if root.left is not None:
                self.find(root.left, expectNumber, memo + [root.val])
            if root.right is not None:
                self.find(root.right, expectNumber, memo + [root.val])

    def FindPath(self, root, expectNumber):
        if root is not None:
            self.find(root, expectNumber, memo=[])
        return self.results
