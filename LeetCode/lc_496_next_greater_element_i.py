from typing import List
import numpy as np


class Solution:
    @staticmethod
    def build_inverse_lookup_table(nums):
        return {v: i for i, v in enumerate(nums)}

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = len(nums1), len(nums2)
        if n1 == 0:
            return []
        lut = self.build_inverse_lookup_table(nums2)  # optimized: put it into for loop @ line17
        stack = [0]  # stores index (position)
        next_greater = [-1] * n2
        for i in range(1, n2):
            while stack and nums2[i] > nums2[stack[-1]]:
                next_greater[stack.pop()] = i
            stack.append(i)
        ans = []
        for i in nums1:
            idx = next_greater[lut[i]]
            ng = -1 if idx == -1 else nums2[idx]
            ans.append(ng)
        return ans


if __name__ == "__main__":
    nums2 = np.random.choice(200, size=100, replace=False)
    nums1 = np.random.permutation(nums2)[:99]

    # nums1 = [18, 8, 2, 17, 13]
    # nums2 = [6, 3, 14, 17, 2, 0, 8, 10, 13, 18]
    print(nums1.tolist())
    print(nums2.tolist())
    print(Solution().nextGreaterElement(nums1, nums2))