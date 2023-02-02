# 115. Distinct Subsequences

## 0. 题目原描述
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.


Example 1:
> Input: s = "rabbbit", t = "rabbit"
> Output: 3
> Explanation:
> As shown below, there are 3 ways you can generate "rabbit" from s.
> rabbbit
> rabbbit
> rabbbit

Example 2:
> Input: s = "babgbag", t = "bag"
> Output: 5
> Explanation:
> As shown below, there are 5 ways you can generate "bag" from s.
> babgbag
> babgbag
> babgbag
> babgbag
> babgbag

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.

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

### method 1
与LCS（最长公共子串）有点像。在用dp计算LCS的时候，其实是已经算过所有的状态（情况）了，那么如果最长公共子串的长度等于t的长度，我们就知道s中肯定是包含t的，那至于有几种不同的方案，可以看这些所有的状态中满足最长公共子串长度等于len(t)的不同路径有多少条（用回溯法即可）。

这个方法虽然可以得到正确答案，但是第二个环节“回溯”会花费过长的时间而超时，因为遍历的量实在是太大了。

### method 2
直接使用DP来解决问题