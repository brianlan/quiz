from typing import List
import numpy as np


class Solution:
    """Merge 2 arrays, then find median."""

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        if i < len(nums1):
            merged.extend(nums1[i:])
        if j < len(nums2):
            merged.extend(nums2[j:])
        if not merged:
            return 0
        if len(merged) % 2 == 1:  # odd
            return merged[len(merged) // 2]
        else:  # even
            return (merged[len(merged) // 2 - 1] + merged[len(merged) // 2]) / 2


class Solution2:
    """Turn problem into find k-th smallest elements in two sorted arrays"""
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if (n1 + n2) % 2 == 0:  # even
            med = (
                Solution2.findKthSmallest(nums1, nums2, (n1 + n2) // 2)
                + Solution2.findKthSmallest(nums1, nums2, (n1 + n2) // 2 + 1)
            ) / 2
        else:  # odd
            med = Solution2.findKthSmallest(nums1, nums2, (n1 + n2) // 2 + 1)
        return med

    @staticmethod
    def findKthSmallest(nums1: List[int], nums2: List[int], k: int):
        """ Kth: value should be strictly possitive
        return
          - array index indicating it's from nums1 or nums2
          - element index in the
        """
        assert k > 0
        if not nums1:
            return nums2[k - 1]
        if not nums2:
            return nums1[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        pos = k // 2 - 1
        if nums1[pos] <= nums2[pos]:
            return Solution2.findKthSmallest(
                nums1[pos + 1 :], nums2, k - len(nums1[: pos + 1])
            )
        else:
            return Solution2.findKthSmallest(
                nums1, nums2[pos + 1 :], k - len(nums2[: pos + 1])
            )


if __name__ == "__main__":
    nums1 = np.sort(np.random.randint(100, size=1))
    nums2 = np.sort(np.random.randint(100, size=11))
    print(nums1.tolist(), nums2.tolist())
    print(Solution2().findMedianSortedArrays(nums1.tolist(), nums2.tolist()))
    # nums1, nums2 = [0, 5, 7, 8, 8, 9], [2, 4, 5, 6, 7, 8]
    # print(nums1, nums2)
    # print(Solution2().findMedianSortedArrays(nums1, nums2))
    # nums1, nums2 = [1, 2, 7, 9, 9], [1, 2, 3, 4, 5, 8]
    # print(nums1, nums2)
    # print(Solution2().findMedianSortedArrays(nums1, nums2))
