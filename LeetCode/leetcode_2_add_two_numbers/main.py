# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        cur = None
        cache = 0
        while l1 is not None or l2 is not None:
            new_val = (l1 or ListNode()).val + (l2 or ListNode()).val + cache
            cache, new_val = new_val // 10, new_val % 10
            new_node = ListNode(new_val)
            if head is None:
                head = new_node
                cur = head
            else:
                cur.next = new_node
                cur = cur.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if cache > 0:
            cur.next = ListNode(cache)
            cur = cur.next
        return head
