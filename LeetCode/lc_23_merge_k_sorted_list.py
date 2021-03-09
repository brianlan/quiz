from common import *


class Solution:
    @staticmethod
    def merge_two_lists(head_a: ListNode, head_b: ListNode) -> ListNode:
        if head_a is None:
            return head_b
        if head_b is None:
            return head_a
        merged = ListNode("sentinel")
        pa, pb, pm = head_a, head_b, merged
        while pa is not None and pb is not None:
            if pa.val <= pb.val:
                pm.next = pa
                pa = pa.next
            else:
                pm.next = pb
                pb = pb.next
            pm = pm.next
        if pa is not None:
            pm.next = pa
        if pb is not None:
            pm.next = pb
        merged = merged.next
        return merged

    @staticmethod
    def get_list_length(head: ListNode) -> int:
        if head is None:
            return 0
        cnt = 0
        while head is not None:
            head = head.next
            cnt += 1
        return cnt

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        lists_w_len = [PrioritizedItem(Solution.get_list_length(l), l) for l in lists if l is not None]
        if len(lists_w_len) == 0:
            return None
        heapq.heapify(lists_w_len)
        for _ in range(len(lists_w_len) - 1):
            # logger.debug(f"\n{[linked_list_to_nums(l) for l in lists]}")
            a = heapq.heappop(lists_w_len)
            b = heapq.heappop(lists_w_len)
            merged_list = Solution.merge_two_lists(a.item, b.item)  # from two shortest
            heapq.heappush(lists_w_len, PrioritizedItem(a.priority + b.priority, merged_list))
        return lists_w_len[0].item
        


if __name__ == "__main__":
    lists = [
        [],
        [2, 3, 10, 12, 16, 18],
        [1, 2, 3, 5],
        [2],
        [10],
        [],
        [15, 16, 17, 21, 23],
        [6, 12, 18, 24, 36],
        [2, 4, 6, 8],
        [3, 5, 6, 7, 8, 9],
    ]
    lists = [create_linked_list(l) for l in lists]
    lists = [None]
    logger.info(linked_list_to_nums(Solution().mergeKLists(lists)))
