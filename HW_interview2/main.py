class Solution:
    def __init__(self) -> None:
        self.memo = [set()]

    def new_subsets(self, num):
        return [s | {num} for s in self.memo]

    def subsets(self, nums):
        if len(nums) > 0:
            for num in nums:
                self.memo.extend(self.new_subsets(num))
        return self.memo


if __name__ == "__main__":
    nums = [1, 2, 3]
    ans = Solution().subsets(nums)
    print(len(ans))
    print(ans)
