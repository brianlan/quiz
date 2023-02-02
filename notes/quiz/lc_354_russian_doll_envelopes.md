# 354. Russian Doll Envelopes

## 0. 题目原描述

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

Example 1:
> Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
> Output: 3
> Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

## 1. 具体->抽象转化模型 - 题目，数学的、符号的、形式化的描述



## 2. 特性提取模型 - 问题有哪些关键特点、特性（不是那种平凡的，而是稍微有点insight的、可能成为突破口的那些）

1. no pre-defined order for these evelopes
1. input evelopes can be sorted only according to either width or height.
1. input evelopes can also be sorted first by width then height, or vice versa. For example: `[5,4],[6,4],[6,7],[2,3] => [2,3],[4,5],[4,6],[7,6]`
1. if we sort by width first then height, the problem is now converted to "longest increasing subsequence", with comparing using 2 numbers as the only difference.
1. **DP:state** 
1. **DP:overlapping subproblems** 
1. **DP:optimal substructure**
1. **DP:state transition function**


## 3. BF解法模型 - 一种BF的思路



## 4. 性能分析模型 - BF中哪个环节拖累了性能（并判断是否可优化），其他还有哪些地方是可优化的



## 5. 方法库匹配模型 - 已知的某种方法（或其类似物，或变化情况），有实现思路且可实现一种新方法
DP