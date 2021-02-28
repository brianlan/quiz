from common import *


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        logger.debug(f"{linked_list_to_nums(head)}")
        if head is None or head.next is None:
            return head
        p1, p2 = head, head.next
        p1_prev = None
        last_node = None
        while p2 is not None:
            if p1.val != p2.val:
                if p1.next is p2:  # non-duplicated
                    p1_prev = p1
                else:  # duplicated
                    if p1_prev is None:
                        head = p2
                    else:
                        p1_prev.next = p2
                p1 = p2
            
            if p2.next is None:
                last_node = p2
            
            p2 = p2.next
        
        if p1 is not last_node and p1.val == last_node.val:
            if p1_prev is None:
                head = last_node.next
            else:
                p1_prev.next = last_node.next

        # logger.debug(f"\n{linked_list_to_nums(head)}")
        return head


if __name__ == "__main__":
    # head = create_linked_list([1, 2, 3, 3, 4, 4, 5])
    # head = create_linked_list([1, 2, 2, 3, 3, 4])
    # head = create_linked_list([1, 2, 2, 3, 4])
    # head = create_linked_list([1, 1, 2, 2])
    # head = create_linked_list([1, 1, 1, 2, 3])
    # head = create_linked_list([1])
    # head = create_linked_list([1, 2])
    # head = create_linked_list([])
    head = create_linked_list(sorted(np.random.randint(20, size=30)))
    logger.info(linked_list_to_nums(Solution().deleteDuplicates(head)))
