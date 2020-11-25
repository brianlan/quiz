from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if len(nums) == 1:
            return [nums]
        if len(nums) == 0:
            return []
        permutations = []
        for i in range(n):
            permutations.extend(
                [
                    [nums[i]] + sub for sub in self.permuteUnique(nums[:i] + nums[i + 1 :])
                ]
            )
        deduped = {tuple(p) for p in permutations}
        return list([list(p) for p in deduped])


if __name__ == "__main__":
    print(Solution().permuteUnique([1, 1, 2, 3]))
