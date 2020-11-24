# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return
        if len(pre) == len(tin) == 1:
            assert pre[0] == tin[0]
            return TreeNode(pre[0])
        root_val = pre[0]
        root_pos_in_tin = tin.index(root_val)
        left_tin = tin[:root_pos_in_tin]
        right_tin = tin[root_pos_in_tin+1:]
        left_pre = pre[1:1+len(left_tin)]
        right_pre = pre[-len(right_tin):]
        root_node = TreeNode(root_val)
        root_node.left = self.reConstructBinaryTree(left_pre, left_tin)
        root_node.right = self.reConstructBinaryTree(right_pre, right_tin)
        return root_node


if __name__ == "__main__":
    tree = Solution().reConstructBinaryTree(
        [1, 2, 3, 4, 6, 5, 7, 8, 9, 11, 10, 12, 13],
        [2, 6, 4, 3, 7, 5, 1, 9, 11, 8, 12, 10, 13]
    )
    a = 100