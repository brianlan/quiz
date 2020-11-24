# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        """
        遍历链表，将每一个数顺序地存在一个list中，
        然后利用reversed函数将其逆序，再返回
        """
        p = listNode
        data = []
        while p is not None:
            data.append(p.val)
            p = p.next
        return list(reversed(data))


class Solution2:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        """
        对链表做逆序，然后遍历该逆序后的链表，输出答案
        """
        pass


if __name__ == "__main__":
    data = ListNode(67)
    data.next = ListNode(0)
    data.next.next = ListNode(24)
    data.next.next.next = ListNode(58)
    Solution2().printListFromTailToHead()
