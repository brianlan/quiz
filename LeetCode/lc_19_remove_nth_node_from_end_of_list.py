from common import *


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        logger.debug(f"\n{linked_list_to_nums(head)}\n{n}")
        fast = head
        to_remove = head
        prev_to_remove = None
        for _ in range(n):
            fast = fast.next
        while fast is not None:
            fast = fast.next
            prev_to_remove = to_remove
            to_remove = to_remove.next
        if prev_to_remove is None:
            head = head.next
        else:
            prev_to_remove.next = to_remove.next
        return head


if __name__ == "__main__":
    # head, n = create_linked_list([1,2,3,4,5]), 2
    # head, n = create_linked_list([1]), 1
    # head, n = create_linked_list([1, 2]), 1
    head, n = create_linked_list(np.random.randint(100, size=10)), np.random.randint(10) + 1
    logger.info(linked_list_to_nums(Solution().removeNthFromEnd(head, n)))
