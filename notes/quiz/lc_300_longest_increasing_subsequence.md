# 300. Longest Increasing Subsequence

## 0. 题目原描述

Given an integer array nums, return the length of the longest strictly increasing subsequence.

## 1. 具体->抽象转化模型 - 题目，数学的、符号的、形式化的描述
input: integer array `nums`
output: a subsequence (doesn't have to be consecutive) `s` consists of nums[i_1], nums[i_2], ..., nums[i_k]
        where i_1 < i_2 < ... < i_k and nums[i_1] < nums[i_2] < ... < nums[i_k] and k <= `length(nums)`

## 2. 特性提取模型 - 问题有哪些关键特点、特性（不是那种平凡的，而是稍微有点insight的、可能成为突破口的那些）
1. Greedy strategy won't work -- when you decide s includes num[i_x], it may cause the rest longer increasing subsequence not be selected.
1. The problem related to 'choices' and 'optimal'
1. k is at least 1 and at most `length(nums)`
1. **DP:state** 
n, `nums[n]` as the last poisition of the LIS.
1. **DP:overlapping subproblems** 
Take `nums[n]` as the last position of the LIS, the longest increasing subsequence's length is F(n), which depends on subproblems F(n-1), F(n-2), ..., F(0); while F(n-2), F(n-3), ..., F(0), so the subproblems got overlapping.
1. **DP:optimal substructure**
if F(n) chooses F(n=5) as the base, we can say F(5) is also the optimal value for the sub-problem. 
1. **DP:state transition function**
F(n=n, m=n) = max(
    (F(n-1) + 1) if nums[n] > nums[n-1] else 1,
    (F(n-2) + 1) if nums[n] > nums[n-2] else 1,
    ...,
    (F(0) + 1) if nums[n] > nums[0] else 1,
)

## 3. BF解法模型 - 一种BF的思路
`nums=[0,1,0,3,2,3]`


dp 0  1  2  3  4  5  6 (n)
-----------------------
   0  1  2  2  3  3  4   


## 4. 性能分析模型 - BF中哪个环节拖累了性能（并判断是否可优化），其他还有哪些地方是可优化的
O(2^(m+n))


## 5. 方法库匹配模型 - 已知的某种方法（或其类似物，或变化情况），有实现思路且可实现一种新方法
DP