from common import *


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] + [-1] * n  # pre[i] stores number of odd numbers as of i, pre[0] === 0, as it means the subarray is []
        cnt = [1] + [0] * (n)  # cnt[i] stores frequency of each pre[i] values as of i. cnt[0] initialized as 1
        num_nice_subarrays = 0
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + int(nums[i - 1] % 2 == 1)
            cnt[pre[i]] += 1
            
            # 最关键的一步思考：
            # 对于位置i，我们是容易知道在i之前总共出现过几个奇数的，但至于这些奇数的位置在哪里, 以及
            # 这些奇数跟i这个位置之间有多少个偶数隔在中间，我们是不容易知道（或说保存）的。这题的解题
            # 思路最妙的点就在于，我们就利用我们容易知道的这个信息，即i之前总共出现过几个奇数: pre[i]，
            # 通过考察pre[i] - pre[j] (j < i)就能知道j和i中间包含了几个奇数。假如i等于4，我们
            # 理论上需要看pre[4]和pre[3], pre[2], pre[1], pre[0]之间的差值，有哪几个是正好
            # 等于k的。假如pre[4] - pre[1]和pre[4] - pre[0]都正好等于k，那么我们就知道到i
            # 这个位置时，我们又新发现了两个nice_subarray, 分别为nums[:4]以及nums[1:4]. 
            # 可是，如果真的这么做，我们就引入了额外的一层循环，使得整个计算复杂度提升为O(n^2).
            # 所以，一个取巧的方式就是用哈希表来存储所有位置j的pre[j]的次数 (注意到，比如pre[2]和pre[3]
            # 的值可能都为1，那么counter[1]就等于2)，而检查pre[i] - pre[j]是否
            # 为k这一动作可以转化为pre[i] - k出现的次数. 举例，pre[4]如果等于4，k等于3，那么就
            # 是去看counter[pre[4] - 3]的值是几，也就是counter[1]的值是几.
            num_nice_subarrays += cnt[pre[i] - k]
        logger.debug(pre)
        logger.debug(cnt)
        return num_nice_subarrays


if __name__ == "__main__":
    nums, k = [8, 5, 2, 2, 5, 1, 3, 5, 5, 1], 3
    # nums, k = [1,1,2,1,1], 3
    # nums, k = [2,4,6], 1
    # nums, k = [2,2,2,1,2,2,1,2,2,2], 2
    # nums, k = [1,1,1,1,1], 1
    # nums, k = (np.random.randint(20, size=10) + 1).tolist(), np.random.randint(10) + 1
    logger.debug(nums)
    logger.debug(k)
    print(Solution().numberOfSubarrays(nums, k))
