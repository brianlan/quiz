import numpy as np

m = int(input())
nums = list(map(int, input().split()))

if m < 2:
    print("-1")

if any([(n < 1 or n > 500) for n in nums]):
    print("-1")


_sum = sum(nums)
quota = _sum // 2
# print(_sum, quota)

dp = [[0] * (quota + 1) for _ in range(m + 1)]
# print(np.array(dp))

for i in range(1, m + 1):
    for j in range(1, quota + 1):
        if j >= nums[i - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i - 1]] + nums[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

opt = dp[-1][-1]
other = _sum - opt
ans = max(opt, other) - min(opt, other)
print(ans)
# print(np.array(dp))

# 5 10 8 2 10
# 10 2 4 8 30 300
# 2 400 4