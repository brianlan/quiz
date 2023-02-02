# 72. Edit Distance

## 0. 题目原描述
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character

Example 1
> Input: word1 = "horse", word2 = "ros"
> Output: 3
> Explanation: 
> horse -> rorse (replace 'h' with 'r')
> rorse -> rose (remove 'r')
> rose -> ros (remove 'e')

Example 2
> Input: word1 = "intention", word2 = "execution"
> Output: 5
> Explanation: 
> intention -> inention (remove 't')
> inention -> enention (replace 'i' with 'e')
> enention -> exention (replace 'n' with 'x')
> exention -> exection (replace 'n' with 'c')
> exection -> execution (insert 'u')


## 1. 具体->抽象转化模型 - 题目，数学的、符号的、形式化的描述

## 2. 特性提取模型 - 问题有哪些关键特点、特性（不是那种平凡的，而是稍微有点insight的、可能成为突破口的那些）
1. **DP:state** 
(i, j)
1. **DP:overlapping subproblems** 
D(i, j) denotes the edit distance between word1[:i] and word2[:j]
1. **DP:optimal substructure**

1. **DP:state transition function**
D(i, j) = min(
    int(word1[i] != word2[j]) + D(i - 1, j - 1),
    1 + D(i, j - 1),
    1 + D(i - 1, j),
)



## 3. BF解法模型 - 一种BF的思路

## 4. 性能分析模型 - BF中哪个环节拖累了性能（并判断是否可优化），其他还有哪些地方是可优化的

## 5. 方法库匹配模型 - 已知的某种方法（或其类似物，或变化情况），有实现思路且可实现一种新方法
